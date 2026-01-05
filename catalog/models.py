from django.db import models


PRODUCT_ICON_CHOICES = [
    ("default", "Default"),
    ("fortnite", "Fortnite"),
    ("valorant", "Valorant"),
    ("spotify", "Spotify"),
    ("youtube", "YouTube"),
    ("steam", "Steam"),
    ("playstation", "PlayStation"),
]



class Region(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    # Display
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # Optional: you can show an indicative price, even though you don't sell directly
    price_eur = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    # Affiliate-only
    affiliate_url = models.URLField(blank=True, help_text="Partner/Affiliate Link (Weiterleitung)")
    active = models.BooleanField(default=True)

    icon_key = models.CharField(
        max_length=20,
        choices=PRODUCT_ICON_CHOICES,
        default="default",
    )
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
