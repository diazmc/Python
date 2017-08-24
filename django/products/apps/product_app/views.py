from django.shortcuts import render
from .models import Product

def index(request):
    product = Product.objects.create(name="book", description="codingdojo", price=2, cost=1)
    product = Product.objects.create(name="laptop", description="dojo", price=4, cost=3)
    product = Product.objects.create(name="phone", description="verizon", price=100, cost=5)
    products = Product.objects.all()

    for product in products:
        print product.name, product.description, product.price, product.cost

    return render(request, 'product_app/index.html')