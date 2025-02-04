from django import forms
from django.core.exceptions import ValidationError
from django.db import models


class Obavijest(models.Model):
    naslov = models.CharField(max_length=100, null=False, blank=False)
    pod_naslov = models.CharField(max_length=150, null=False, blank=True)
    tekst = models.CharField(null=False, blank=True)
    slika = models.ImageField(upload_to='obavijest_slike',null=False, blank=True)
    url = models.CharField(max_length=512, null=True, blank=True)


    def __str__(self):
        return self.naslov

    class Meta:
        verbose_name_plural = "Obavijesti"

class Glavna_Frizura(models.Model):
    ime = models.CharField(max_length=100, null=True, blank=True)
    cijena = models.IntegerField(null=True, blank=True)
    opis = models.CharField(null=False, blank=True)
    slika = models.ImageField(upload_to='frizure', null=True, blank=True)
    video = models.FileField(upload_to='frizure_video', null=True, blank=True)

    pocetna_stranica = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        abstract = True

    def clean(self):
        if self.slika and self.video:
            raise ValidationError("Ne možete uplodat-i sliku i video. Odaberite jedno.")
        if not self.slika and not self.video:
            raise ValidationError("Moraš uplodat-i sliku ili video.")

    def __str__(self):
        return date


class Zenske_frizure(Glavna_Frizura):
    class Meta:
        verbose_name_plural = "Zenske Frizure"

class Muske_frizure(Glavna_Frizura):
    class Meta:
        verbose_name_plural = "Muske Frizure"

class Djecje_frizure(Glavna_Frizura):
    class Meta:
        verbose_name_plural = "Djecje Frizure"

class Produkti(Glavna_Frizura):
    class Meta:
        verbose_name_plural = "Produkti"
