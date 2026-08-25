"""
Root URLconf fallback (local dev). Per-request routing is handled by SiteBrandMiddleware.
"""
import os

from django.contrib import admin
from django.urls import include, path

_default = os.environ.get("SITE_BRAND", "droobtech").strip().lower()
if _default not in ("droobtech", "visions-tech"):
    _default = "droobtech"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        include("website.urls" if _default == "visions-tech" else "droobtech.urls"),
    ),
]
