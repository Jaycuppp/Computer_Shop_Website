from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.NewProducts),
    path('clearence', views.ClearenceProducts),
    path('return', views.ProductReturns)
]
