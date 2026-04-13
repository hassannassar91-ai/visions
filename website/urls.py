from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("solutions/", views.solutions, name="solutions"),
    path("industries/", views.industries, name="industries"),
    path("products/", views.products, name="products"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),
]
