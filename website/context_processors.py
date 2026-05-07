def company(request):
    return {
        "company_name": "Visions Tech",
    }


def language(request):
    current_language = request.session.get("site_language", "en")
    if current_language not in ("en", "ar"):
        current_language = "en"

    return {
        "site_language": current_language,
        "is_arabic": current_language == "ar",
    }
