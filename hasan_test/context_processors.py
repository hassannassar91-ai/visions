def company(request):
    brand = getattr(request, "site_brand", "droobtech")
    if brand == "visions-tech":
        from website.context_processors import company as visions_company

        return visions_company(request)

    from droobtech.context_processors import company as droobtech_company

    return droobtech_company(request)


def language(request):
    brand = getattr(request, "site_brand", "droobtech")
    if brand == "visions-tech":
        from website.context_processors import language as visions_language

        return visions_language(request)

    from droobtech.context_processors import language as droobtech_language

    return droobtech_language(request)
