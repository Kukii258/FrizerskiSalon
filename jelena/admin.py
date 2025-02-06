from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.admin import helpers

from .models import Obavijest, Zenske_frizure, Muske_frizure, Djecje_frizure, Produkti
from .forms import FileFieldForm  # Ensure correct form is imported


@admin.action(description="Dodaj Mapu Slika")
def import_slike(modeladmin, request, queryset):
    form = None

    if "upload" in request.POST:
        form = FileFieldForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist("file_field")  # Get all uploaded files

            for uploaded_file in files:
                 Zenske_frizure.objects.create(slika=uploaded_file)

            messages.success(request, f"Successfully uploaded {len(files)} files.")
            return HttpResponseRedirect(reverse("admin:jelena_zenske_frizure_changelist"))

    if not form:
        form = FileFieldForm(initial={"_selected_action": request.POST.getlist(helpers.ACTION_CHECKBOX_NAME)})

    return render(request, "html/upload_slike.html", {"upload_form": form})


@admin.register(Zenske_frizure)
class Zenske_frizureAdmin(admin.ModelAdmin):
    actions = [import_slike]

    def changelist_view(self, request, extra_context=None):
        if request.POST.get("action") == "import_slike":
            if not request.POST.getlist(helpers.ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                post.setlist(helpers.ACTION_CHECKBOX_NAME, [str(p.id) for p in Zenske_frizure.objects.all()])
                request.POST = post  # Correct way to override request.POST
        return super().changelist_view(request, extra_context)

    def run_make_slike(self, request):
        import_slike(self, request, None)
        messages.success(request, "Slike uspješno dodane")
        return HttpResponseRedirect(request.headers.get("referer", "/"))



@admin.register(Muske_frizure)
class Muske_frizureAdmin(admin.ModelAdmin):
    pass


@admin.register(Djecje_frizure)
class Djecje_frizureAdmin(admin.ModelAdmin):
    pass


@admin.register(Produkti)
class ProduktiAdmin(admin.ModelAdmin):
    pass
