# Create your views here.
from django.shortcuts import render, get_object_or_404

from .models import Obavijest


def naslovnica(request):

    obavijest = Obavijest.objects.first()

    context = {'obavijest':obavijest}
    return render(request, "html/index.html",context)

def obavijest(request,obavijest_id):
    obavijest = get_object_or_404(Obavijest, pk=obavijest_id)
    return render(request,"html/obavijest.html",{'obavijest':obavijest})
