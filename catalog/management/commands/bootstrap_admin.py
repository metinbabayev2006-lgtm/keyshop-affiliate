import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if os.getenv("BOOTSTRAP_PRODUCTS") != "1":
            return

        if Product.objects.exists():
            return  # schon Produkte da -> nix machen

        call_command("loaddata", "catalog/fixtures/products.json")