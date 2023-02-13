from django.http import HttpResponse
from django.shortcuts import render
from .models import Store

# Index is the Main Page for the Web App of the website


def index(request):
    store = Store.objects.all()
    return render(request, 'index.html', {'Store': store})
