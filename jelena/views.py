# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Obavijest, Zenske_frizure, Muske_frizure, Djecje_frizure, Produkti

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def naslovnica(request):

    if request.method == "POST":
        if request.POST.get("name") != "":
          send_email(request)
    else:
        print("nisamusao")

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





def send_email(request):


    name = request.POST.get("name")
    email = request.POST.get("email")
    potvrda_email = request.POST.get("potvrda_email")
    frizura = request.POST.get("frizura")
    datum = request.POST.get("datum")

    if email != potvrda_email:
        error_message = "Email adresa i potvrda email adrese se ne podudaraju."
        print(email)
        print(potvrda_email)
        return render(request, "html/index.html", {"error_message": error_message})

    sender_email = "salon.jelena.narucivanje@gmail.com"
    sender_password = "aazqbvrsllernrks"
    salon_email = "salon.jelena.narucivanje@gmail.com"

    # Confirmation email to the user
    user_subject = "Potvrda narudžbe termina"
    user_body = f"""
    Poštovani {name},

    Vaša narudžba termina je uspješno zaprimljena. Ovdje su detalji vašeg zahtjeva:

    Ime: {name}
    Frizura: {frizura}
    Datum: {datum}

    Hvala što ste odabrali naš salon! Kontaktirat ćemo vas uskoro kako bismo potvrdili termin.

    Srdačno,
    Salon Jelena
    """

    # Notification email to salon
    salon_subject = "Zaprimljena Narudžba Termina"
    salon_body = f"""
    Poštovani,

    Zaprimljena je nova narudžba termina. Detalji narudžbe su sljedeći:

    Ime: {name}
    Frizura: {frizura}
    Datum: {datum}
    Email: {email}

    Srdačno,
    Sustav Narudžbi Salona
    """

    # Sending emails
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            # Send confirmation email to the user
            user_message = MIMEMultipart()
            user_message["From"] = sender_email
            user_message["To"] = email
            user_message["Subject"] = user_subject
            user_message.attach(MIMEText(user_body, "plain"))
            server.sendmail(sender_email, email, user_message.as_string())

            # Send notification email to the salon
            salon_message = MIMEMultipart()
            salon_message["From"] = sender_email
            salon_message["To"] = salon_email
            salon_message["Subject"] = salon_subject
            salon_message.attach(MIMEText(salon_body, "plain"))
            server.sendmail(sender_email, salon_email, salon_message.as_string())

        print("Emails sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

    # Redirect to naslovnica after sending the emails
    return redirect("naslovnica")
