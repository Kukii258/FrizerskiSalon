# ruff: noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from jelena import views, models
from jelena.admin import custom_admin_site

urlpatterns = [

    #Galerije
    path('zenska-galerija/', views.galerija, {'model': models.Zenske_frizure, 'template_name': 'html/zenska_galerija.html'},
         name='zenska_galerija'),
    path('muska-galerija/', views.galerija, {'model': models.Muske_frizure, 'template_name': 'html/muska_galerija.html'},
         name='muska_galerija'),
    path('djecja-galerija', views.galerija, {'model': models.Djecje_frizure, 'template_name': 'html/djecja_galerija.html'},
         name='djecja_galerija'),
    path('produkti-galerija/', views.galerija, {'model': models.Produkti, 'template_name': 'html/produkti_galerija.html'},
         name='produkti_galerija'),

    #Index
    path("", views.naslovnica, name="naslovnica"),
    path("obavijest/<int:obavijest_id>", views.obavijest, name="obavijest"),
    path("send_email/", views.send_email, name="send_email"),
    path("o_nama",views.o_nama, name="o_nama"),

    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("salon_jelena.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    # ...
    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
