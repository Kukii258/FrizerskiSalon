
from django.contrib import admin

from .models import Obavijest


@admin.register(Obavijest)
class ObavijestAdmin(admin.ModelAdmin):

    pass
