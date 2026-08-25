from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme


def set_language(request):
    lang = (request.GET.get("lang") or "en").lower()
    request.session["site_language"] = "ar" if lang == "ar" else "en"
    next_url = request.GET.get("next") or request.META.get("HTTP_REFERER") or "/"
    if not url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        next_url = "/"
    return redirect(next_url)


def home(request):
    return render(request, "droobtech/home.html")


def about(request):
    return render(request, "droobtech/about.html")


def capabilities(request):
    return render(request, "droobtech/capabilities.html")


def capability_detail(request, slug):
    templates = {
        "digital-transformation": "droobtech/capabilities/digital_transformation.html",
        "data-intelligence-ai": "droobtech/capabilities/data_intelligence_ai.html",
        "enterprise-technology": "droobtech/capabilities/enterprise_technology.html",
        "digital-solution-engineering": "droobtech/capabilities/digital_solution_engineering.html",
        "integration-interoperability": "droobtech/capabilities/integration_interoperability.html",
    }
    template = templates.get(slug)
    if not template:
        return render(request, "droobtech/404.html", status=404)
    return render(request, template)


def solution_detail(request, slug):
    templates = {
        "nexus": "droobtech/solutions/nexus.html",
        "visions-erp": "droobtech/solutions/visions_erp.html",
        "rapid-digital-solutions": "droobtech/solutions/rapid_digital.html",
    }
    template = templates.get(slug)
    if not template:
        return render(request, "droobtech/404.html", status=404)
    return render(request, template)


def industries(request):
    return render(request, "droobtech/industries.html")


def experience(request):
    return render(request, "droobtech/experience.html")


def insights(request):
    return render(request, "droobtech/insights.html")


def why_droobtech(request):
    return render(request, "droobtech/why_droobtech.html")


def contact(request):
    if request.method == "POST":
        is_arabic = request.session.get("site_language") == "ar"
        name = (request.POST.get("name") or "").strip()
        email = (request.POST.get("email") or "").strip()
        message = (request.POST.get("message") or "").strip()
        if not name or not email or not message:
            messages.error(
                request,
                "يرجى تعبئة الاسم والبريد الإلكتروني والرسالة."
                if is_arabic
                else "Please fill in name, business email, and message.",
            )
        else:
            messages.success(
                request,
                "شكراً لك — تم استلام رسالتك، وسنتواصل معك قريباً."
                if is_arabic
                else "Thank you — your message was received. We will get back to you soon.",
            )
            return redirect("contact")
    return render(request, "droobtech/contact.html")


def page_not_found(request, exception=None):
    return render(request, "droobtech/404.html", status=404)
