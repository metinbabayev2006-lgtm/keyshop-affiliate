from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:slug>/", views.category_list, name="category"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("go/<int:pk>/", views.affiliate_redirect, name="affiliate_go"),
    path("impressum/", views.impressum, name="impressum"),
    path("datenschutz/", views.datenschutz, name="datenschutz"),
    path("kontakt/", views.kontakt, name="kontakt"),
]
