from django.http import HttpResponse
from django.shortcuts import render
from .models import MainProducts, SpecialSale, NewProducts

# Index is the Main Page for the Web App of the website


def ProductIndex(request):
    # Some other methods that can be used .save(), .filter(), and .get()
    product = MainProducts.objects.all()
    return render(request, 'ProductIndex.html', {'Products': product})


# New Products Page for brand new and upcoming Products the Shop will carry
def NewProduct(request):
    product = NewProducts.objects.all()
    return render(request, 'NewProduct.html', {'Products': product})


# Clearence Page for products that need to leave the business ASAP
def ClearenceProducts(request):
    product = SpecialSale.objects.all()
    pass


# Setup A Product Return Page like every other Ecommerce Web Store
def ProductReturns(request):
    pass
