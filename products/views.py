from django.http import HttpResponse
from django.shortcuts import render
from .models import MainProducts, SpecialSale, NewProducts

# Index is the Main Page for the Web App of the website
def index(request):
    # Some other methods that can be used .save(), .filter(), and .get()
    product = MainProducts.objects.all()
    return render(request, 'index.html', {'Products': product})


# New Products Page for brand new and upcoming Products the Shop will carry
def brandNew(request):
    product = NewProducts.objects.all()
    return render(request, 'NewProducts.html', {'Products': product})


# Clearence Page for products that need to leave the business ASAP
def ClearenceProducts(request):
    pass


# Setup A Product Return Page like every other Ecommerce Web Store
def ProductReturns(request):
    pass