from django.shortcuts import get_object_or_404, redirect, render
from catalog.models import Product, Category
from django.db.models import Q
from django.db.models import F
from django.shortcuts import render

def about(request):
    return render(request, "shop/about.html")

def how_we_make_money(request):
    return render(request, "shop/how_we_make_money.html")

def apply_sort(products, sort: str):
    if sort == "price_asc":
        # Preis aufsteigend, aber leere Preise (NULL) nach hinten
        return products.order_by(F("price_eur").asc(nulls_last=True), "name")

    if sort == "price_desc":
        # Preis absteigend, leere Preise (NULL) nach hinten
        return products.order_by(F("price_eur").desc(nulls_last=True), "name")

    if sort == "name_asc":
        return products.order_by("name")

    return products.order_by("-id")




def home(request):
    q = request.GET.get("q", "").strip()
    sort = request.GET.get("sort", "")
    region = request.GET.get("region", "").strip()
    current_category = None

    products = Product.objects.filter(active=True).select_related("category", "region")
    categories = Category.objects.all().order_by("name")

    if q:
        products = products.filter(name__icontains=q)

    # region filter expects Region.code in query param (kept compatible with your UI)
    if region:
        products = products.filter(region__code=region)

    products = apply_sort(products, sort)

    return render(request, "shop/home.html", {
        "products": products,
        "categories": categories,
        "current_category": current_category,
        "q": q,
        "sort": sort,
        "region": region,
    })


def category_list(request, slug):
    q = request.GET.get("q", "").strip()
    sort = request.GET.get("sort", "")
    region = request.GET.get("region", "").strip()

    current_category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all().order_by("name")

    products = Product.objects.filter(active=True, category=current_category).select_related("category", "region")

    if q:
        products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))

    if region:
        products = products.filter(region__code=region)

    products = apply_sort(products, sort)

    return render(request, "shop/home.html", {
        "products": products,
        "categories": categories,
        "current_category": current_category,
        "q": q,
        "sort": sort,
        "region": region,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, active=True)
    categories = Category.objects.all().order_by("name")
    # For nav highlight (optional)
    current_category = product.category
    return render(request, "shop/product_detail.html", {
        "product": product,
        "categories": categories,
        "current_category": current_category,
    })


def affiliate_redirect(request, pk):
    product = get_object_or_404(Product, pk=pk, active=True)
    if product.affiliate_url:
        return redirect(product.affiliate_url)
    # Fallback: if no link set, go back to product page
    return redirect("shop:product_detail", pk=product.pk)


def _base_context():
    """Common context for pages that use base.html navigation."""
    return {
        "categories": Category.objects.all().order_by("name"),
        "current_category": None,
    }


def impressum(request):
    ctx = _base_context()
    return render(request, "shop/impressum.html", ctx)


def datenschutz(request):
    ctx = _base_context()
    return render(request, "shop/datenschutz.html", ctx)


def kontakt(request):
    ctx = _base_context()
    return render(request, "shop/kontakt.html", ctx)
