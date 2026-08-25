"""
URL configuration for hasan_test project.

Each Render web service sets SITE_BRAND to select which site this instance serves:
  - visions-tech  → Visions Tech (visions-tek.com)
  - droobtech     → DroobTech Holding (droobtech.sa)
"""
import os

from django.contrib import admin
from django.urls import include, path

SITE_BRAND = os.environ.get("SITE_BRAND", "droobtech").strip().lower()
if SITE_BRAND not in ("droobtech", "visions-tech"):
    SITE_BRAND = "droobtech"

if SITE_BRAND == "visions-tech":
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("website.urls")),
    ]
else:
    handler404 = "droobtech.views.page_not_found"
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("droobtech.urls")),
    ]
