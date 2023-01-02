from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/results/", include("core_apps.dsgres.urls")),
]

admin.site.site_header = "Rozliczenia Ferran"
admin.site.site_title = "Rozliczenia Ferran API Admin Portal"
admin.site.index_title = "Witaj na Rozliczenia Ferran API Portal"