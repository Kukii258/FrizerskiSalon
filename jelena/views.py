# Create your views here.
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
from datetime import datetime

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse

from .models import Obavijest, Zenske_frizure, Muske_frizure, Djecje_frizure, Produkti, Glavna_Frizura

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from django.shortcuts import render

def naslovnica(request):
    # Extract GET parameters from the request
    error_message = request.GET.get('error_message', None)
    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    frizura = request.GET.get('frizura', '')
    datum = request.GET.get('datum', '')
    broj_mobitela = request.GET.get('broj_mobitela', '')
    email_sent = request.GET.get('email_sent', '')

    # Your other logic for fetching data
    obavijesti = Obavijest.objects.all().order_by('-id')[:3]
    zenske_zadnje_slike = zadnje_slike(Zenske_frizure)
    djecje_zadnje_slike = zadnje_slike(Djecje_frizure)
    produkt_zadnje_slike = zadnje_slike(Produkti)

    # Prepare the context for the template
    context = {
        'obavijesti': obavijesti,
        'zenske_zadnje_slike': zenske_zadnje_slike,
        'djecje_zadnje_slike': djecje_zadnje_slike,
        'produkt_zadnje_slike': produkt_zadnje_slike,
        'name': name,
        'email': email,
        'frizura': frizura,
        'datum': datum,
        'broj_mobitela': broj_mobitela,
        'error_message': error_message,  # Include error message if available
        'email_sent': email_sent
    }

    return render(request, "html/index.html", context)

def zadnje_slike(model):
    slike = model.objects.filter(pocetna_stranica=True).exclude(slika="").order_by("-id")[:4]

    modified_slike = []

    for slika in slike:
        slika_obj = model.objects.get(id=slika.id)
        img = Image.open(slika_obj.slika)

        width, height = img.size

        if width != height:
            min_dimension = min(width, height)


            left = (width - min_dimension) // 2
            top = (height - min_dimension) // 2
            right = left + min_dimension
            bottom = top + min_dimension

            img = img.crop((left, top, right, bottom))

            buffer = BytesIO()
            img.save(buffer, format="JPEG")
            slika_obj.slika.save(f"cropped_{slika.id}.jpg", ContentFile(buffer.getvalue()), save=True)

        modified_slike.append(slika_obj)

    return modified_slike


def obavijest(request,obavijest_id):
    obavijest = get_object_or_404(Obavijest, pk=obavijest_id)
    return render(request,"html/obavijest.html",{'obavijest':obavijest})


def galerija(request, model, template_name):
    slike = model.objects.all()
    context = {'slike': slike}
    return render(request, template_name, context)

from django.shortcuts import render, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    potvrda_email = request.POST.get("potvrda_email", "")
    frizura = request.POST.get("frizura", "")
    datum = request.POST.get("datum", "")
    broj_mobitela = request.POST.get("broj_mobitela", "")

    if datum:
        parsed_date = datetime.strptime(datum, "%Y-%m-%d")
        datum = parsed_date.strftime("%d/%m/%Y")

    # Check for email mismatch
    if email != potvrda_email:
        error_message = "Email adresa i potvrda email adrese se ne podudaraju."
        if email != potvrda_email:
            error_message = "Email adresa i potvrda email adrese se ne podudaraju."

            # Redirect to 'naslovnica' view with query parameters
            return redirect(
                reverse(
                    'naslovnica') + f'?error_message={error_message}&name={name}&email={email}&frizura={frizura}&datum={datum}&broj_mobitela={broj_mobitela}'
            )

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
    Broj mobitela: {broj_mobitela}
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
        # Return with a flag indicating success
        return redirect(
            reverse(
                'naslovnica') + f'?email_sent={True}'
        )
    except Exception as e:
        print(f"Error: {e}")
        return redirect(
            reverse(
                'naslovnica') + f'?error_message={error_message}&name={name}&email={email}&frizura={frizura}&datum={datum}&broj_mobitela={broj_mobitela}'
        )



def o_nama(request):
    return render(request, "html/about.html")
