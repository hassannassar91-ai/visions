from django.contrib import messages
from django.shortcuts import redirect, render


def home(request):
    return render(request, "website/home.html")


def about(request):
    return render(request, "website/about.html")


def solutions(request):
    return render(request, "website/solutions.html")


def industries(request):
    return render(request, "website/industries.html")


def products(request):
    return render(request, "website/products.html")


def projects(request):
    return render(request, "website/projects.html")


def contact(request):
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        email = (request.POST.get("email") or "").strip()
        message = (request.POST.get("message") or "").strip()
        if not name or not email or not message:
            messages.error(
                request,
                "Please fill in full name, email address, and message.",
            )
        else:
            messages.success(
                request,
                "Thank you — your message was received. We will get back to you soon.",
            )
            return redirect("contact")
    return render(request, "website/contact.html")
