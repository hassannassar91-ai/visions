from django.contrib import admin
from django.urls import include, path

handler404 = "droobtech.views.page_not_found"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("droobtech.urls")),
]
