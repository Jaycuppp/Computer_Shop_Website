from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# The Main Product Page
def index(request):
    # Some other methods that can be used .save(), .filter(), and .get()
    product = Product.objects.all()
    return render(request, 'index.html', {'Products': product})


# New Products Page for brand new and upcoming Products the Shop will carry
def NewProducts(request):
    pass


# Clearence Page for products that need to leave the business ASAP
def ClearenceProducts(request):
    pass


# Setup A Product Return Page like every other Ecommerce Web Store
def ProductReturns(request):
    pass
