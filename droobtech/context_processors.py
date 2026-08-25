def company(request):
    return {
        "company_name": "DroobTech Holding",
        "company_name_ar": "دروب تك القابضة",
        "company_descriptor_en": "Saudi Investment & Technology Group",
        "company_descriptor_ar": "مجموعة سعودية للاستثمار والتقنية",
        "tagline_en": "Building Connected, Intelligent Enterprises.",
        "tagline_ar": "نبني مؤسسات مترابطة وذكية.",
        "positioning_en": "Enterprise Technology • Digital Transformation • Data Intelligence & AI",
        "positioning_ar": "تقنيات المؤسسات • التحول الرقمي • ذكاء البيانات والذكاء الاصطناعي",
        "website_url": "www.droobtech.sa",
        "contact_email": "info@droobtech.sa",
        "address_en": "Almohamadia Tower, Al Khobar, Kingdom of Saudi Arabia",
        "address_ar": "برج المحمدية، الخبر، المملكة العربية السعودية",
    }


def language(request):
    current_language = request.session.get("site_language", "en")
    if current_language not in ("en", "ar"):
        current_language = "en"

    return {
        "site_language": current_language,
        "is_arabic": current_language == "ar",
    }
