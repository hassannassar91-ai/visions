from django.conf import settings

from .site_brand import URLCONFS, brand_for_host


class SiteBrandMiddleware:
    """Select site by request hostname, falling back to SITE_BRAND env."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        brand = brand_for_host(request.get_host())
        if brand is None:
            brand = getattr(settings, "SITE_BRAND", "droobtech")
        request.site_brand = brand
        request.urlconf = URLCONFS[brand]
        return self.get_response(request)
