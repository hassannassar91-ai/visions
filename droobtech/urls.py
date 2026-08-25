from django.urls import path

from . import views

urlpatterns = [
    path("set-language/", views.set_language, name="set_language"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("capabilities/", views.capabilities, name="capabilities"),
    path(
        "capabilities/<slug:slug>/",
        views.capability_detail,
        name="capability_detail",
    ),
    path("solutions/<slug:slug>/", views.solution_detail, name="solution_detail"),
    path("industries/", views.industries, name="industries"),
    path("experience/", views.experience, name="experience"),
    path("insights/", views.insights, name="insights"),
    path("why-droobtech/", views.why_droobtech, name="why_droobtech"),
    path("contact/", views.contact, name="contact"),
]
