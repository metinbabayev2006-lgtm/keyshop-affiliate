from django.contrib import admin
from .models import Product, Category, Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")
    ordering = ("code",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "region", "active")
    list_filter = ("active", "category", "region")
    search_fields = ("name", "description", "affiliate_url")
    ordering = ("name",)

    fieldsets = (
        ("Produkt", {"fields": ("name", "description", "icon_key", "category", "region", "active")}),
        ("Affiliate", {"fields": ("affiliate_url", "price_eur")}),
    )
