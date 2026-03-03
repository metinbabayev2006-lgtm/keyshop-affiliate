from django.contrib import admin, messages
from django.core.management import call_command
from django.http import HttpResponseRedirect
from django.urls import path

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

    # ✅ Button im Admin anzeigen
    change_list_template = "admin/catalog/product_changelist.html"

    # ✅ Fix: Filter im Admin (rechts) auch bei breiten Screens erzwingen
    class Media:
        css = {"all": ("admin/custom.css",)}

    # ✅ Extra Admin-URL: /admin/catalog/product/import-fixture/
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("import-fixture/", self.admin_site.admin_view(self.import_fixture)),
        ]
        return my_urls + urls

    # ✅ Importiert: catalog/fixtures/products.json
    def import_fixture(self, request):
        try:
            call_command("loaddata", "catalog/fixtures/products.json")
            messages.success(request, "Produkte erfolgreich importiert ✅")
        except Exception as e:
            messages.error(request, f"Import fehlgeschlagen: {e}")
        return HttpResponseRedirect("../")
