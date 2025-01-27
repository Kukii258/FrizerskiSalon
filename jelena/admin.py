
from django.contrib import admin

from .models import *
from .forms import *

@admin.register(Obavijest)
class ObavijestAdmin(admin.ModelAdmin):

    pass

@admin.register(Zenske_frizure)
class Zenske_frizureAdmin(admin.ModelAdmin):
    form = frizura_form

@admin.register(Muske_frizure)
class Muske_frizureAdmin(admin.ModelAdmin):
    form = frizura_form

@admin.register(Djecje_frizure)
class Djecje_frizureAdmin(admin.ModelAdmin):
    form = frizura_form

@admin.register(Produkti)
class ProduktiAdmin(admin.ModelAdmin):
    form = frizura_form
