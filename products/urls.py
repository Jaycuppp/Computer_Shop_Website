from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.brandNew),
    path('clearence', views.ClearenceProducts),
    path('return', views.ProductReturns)
]