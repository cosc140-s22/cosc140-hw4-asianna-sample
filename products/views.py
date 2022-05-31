from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Product


def index(request):
    products = Product.objects.all().order_by('name')
    return render(request,
                  "products/index.html",
                  context={"products": products})


def show(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/show.html", context={"product": product})
