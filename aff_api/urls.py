from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/results/", include("core_apps.dsgres.urls")),
    path("api/v1/nickname/", include("core_apps.nickname.urls")),
]

admin.site.site_header = "Settlements"
admin.site.site_title = "Settlements API Admin Portal"
admin.site.index_title = "Settlements API Portal"