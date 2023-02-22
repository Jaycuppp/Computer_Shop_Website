from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def HomePage(request):
    return render(request, 'HomeIndex.html')