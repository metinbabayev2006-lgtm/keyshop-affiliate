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
    path("ueber-uns/", views.about, name="about"),
    path("wie-wir-geld-verdienen/", views.how_we_make_money, name="how_we_make_money"),

]
