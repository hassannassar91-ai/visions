"""Host → site brand mapping for multi-site deployment."""

VISIONS_TECH_HOSTS = frozenset(
    {
        "visions-tek.com",
        "www.visions-tek.com",
        "visions-tek-web.onrender.com",
    }
)

DROOBTECH_HOSTS = frozenset(
    {
        "droobtech.sa",
        "www.droobtech.sa",
        "droobtech.onrender.com",
    }
)

URLCONFS = {
    "visions-tech": "hasan_test.urls_visions",
    "droobtech": "hasan_test.urls_droobtech",
}


def brand_for_host(host: str) -> str | None:
    hostname = host.split(":")[0].lower()
    if hostname in VISIONS_TECH_HOSTS:
        return "visions-tech"
    if hostname in DROOBTECH_HOSTS:
        return "droobtech"
    return None
