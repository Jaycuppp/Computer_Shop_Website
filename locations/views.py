from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Store


def LocationIndex(request):
    store = Store.objects.all()
    return render(request, 'LocationIndex.html', {'Store': store})
