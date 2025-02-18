import os

from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.admin import helpers

from .models import Obavijest, Zenske_frizure, Muske_frizure, Djecje_frizure, Produkti
from .forms import FileFieldForm  # Ensure correct form is imported
from .users.models import User


@admin.action(description="Dodaj Mapu Slika")
def import_slike(modeladmin, request, queryset):
    form = None

    if "upload" in request.POST:
        form = FileFieldForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist("file_field")  # Get all uploaded files

            for uploaded_file in files:
                modeladmin.model.objects.create(slika=uploaded_file)

            messages.success(request, f"Successfully uploaded {len(files)} files.")

            # Dynamically redirect to the correct model's changelist page
            model_meta = modeladmin.model._meta
            return HttpResponseRedirect(reverse(f"admin:{model_meta.app_label}_{model_meta.model_name}_changelist"))

    if not form:
        form = FileFieldForm(initial={"_selected_action": request.POST.getlist(helpers.ACTION_CHECKBOX_NAME)})

    return render(request, "html/upload_slike.html", {"upload_form": form})


from django.utils.html import format_html

class BaseFrizureAdmin(admin.ModelAdmin):
    """Base admin configuration for all Frizure models."""

    actions = [import_slike]
    list_display = ("get_ime_or_filename", "media_display", "datum_uploada")

    @admin.display(
        description="Ime"
    )
    def get_ime_or_filename(self, obj):
        """Returns the name if available, otherwise the image/video filename."""
        if obj.ime:
            return obj.ime
        elif obj.slika:
            return os.path.basename(obj.slika.name) if obj.slika else "-"
        elif obj.video:
            return os.path.basename(obj.video.name) if obj.video else "-"
        return "-"


    @admin.display(
        description="Slika"
    )
    def media_display(self, obj):
        """Displays the image if available, otherwise a video camera icon."""
        if obj.slika:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.slika.url)
        elif obj.video:
            return format_html('<span style="font-size: 24px;">📹</span>')  # Video camera icon
        return "-"


    def changelist_view(self, request, extra_context=None):
        """Ensures bulk selection of all items when importing images."""
        if request.POST.get("action") == "import_slike":
            if not request.POST.getlist(helpers.ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                post.setlist(helpers.ACTION_CHECKBOX_NAME, [str(p.id) for p in self.model.objects.all()])
                request.POST = post
        return super().changelist_view(request, extra_context)

    def run_make_slike(self, request):
        """Runs the import_slike action and refreshes the page."""
        import_slike(self, request, None)
        messages.success(request, "Slike uspješno dodane")
        return HttpResponseRedirect(request.headers.get("referer", "/"))

@admin.register(Zenske_frizure)
class Zenske_frizureAdmin(BaseFrizureAdmin):
 pass


@admin.register(Muske_frizure)
class Muske_frizureAdmin(BaseFrizureAdmin):
    pass


@admin.register(Djecje_frizure)
class Djecje_frizureAdmin(BaseFrizureAdmin):
    pass


@admin.register(Produkti)
class ProduktiAdmin(BaseFrizureAdmin):
    pass

@admin.register(Obavijest)
class ObavijestAdmin(admin.ModelAdmin):
    pass

from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _


class CustomAdminSite(AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of apps and their models.
        This method will allow you to control the order of the models in the left sidebar.
        """
        app_list = super().get_app_list(request)

        # Custom model order using the model's `_meta.model_name`
        custom_order = [
            "obavijest",  # Correct model name for Obavijest
            "zenske_frizure",  # Correct model name for Zenske_frizure
            "muske_frizure",  # Correct model name for Muske_frizure
            "djecje_frizure",  # Correct model name for Djecje_frizure
            "produkti",  # Correct model name for Produkti
        ]

        # Sort the app list according to the custom_order
        for app in app_list:
            app['models'].sort(key=lambda x: custom_order.index(x['object_name'].lower()) if x[
                                                                                                 'object_name'].lower() in custom_order else len(
                custom_order))

        return app_list


# Instantiate the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

# Register your models with the custom admin site
custom_admin_site.register(Zenske_frizure, Zenske_frizureAdmin)
custom_admin_site.register(Muske_frizure, Muske_frizureAdmin)
custom_admin_site.register(Djecje_frizure, Djecje_frizureAdmin)
custom_admin_site.register(Produkti, ProduktiAdmin)
custom_admin_site.register(Obavijest, ObavijestAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Your user admin configuration here
    pass
