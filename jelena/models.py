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
