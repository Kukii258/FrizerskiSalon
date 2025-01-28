# Create your views here.
from django.shortcuts import render, get_object_or_404

from .models import Obavijest, Zenske_frizure, Muske_frizure, Djecje_frizure, Produkti


def naslovnica(request):

    obavijesti = Obavijest.objects.all().order_by('-id')[:3]

    zenske_zadnje_slike = zadnje_slike(Zenske_frizure)
    djecje_zadnje_slike = zadnje_slike(Djecje_frizure)
    produkt_zadnje_slike = zadnje_slike(Produkti)


    context = {'obavijesti':obavijesti,'zenske_zadnje_slike':zenske_zadnje_slike, 'djecje_zadnje_slike':djecje_zadnje_slike, 'produkt_zadnje_slike':produkt_zadnje_slike}
    return render(request, "html/index.html",context)


def zadnje_slike(model):
    return model.objects.filter(pocetna_stranica=True).exclude(slika="").order_by("-id")[:4]

def obavijest(request,obavijest_id):
    obavijest = get_object_or_404(Obavijest, pk=obavijest_id)
    return render(request,"html/obavijest.html",{'obavijest':obavijest})


def galerija(request, model, template_name):
    slike = model.objects.all()
    context = {'slike': slike}
    return render(request, template_name, context)
