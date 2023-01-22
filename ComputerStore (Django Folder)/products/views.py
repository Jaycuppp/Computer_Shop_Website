from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    # Some other methods that can be used .save(), .filter(), and .get()
    product = Product.objects.all()
    return render(request, 'index.html', {'Products': product})

def NewProducts(request):
    pass