from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductIndex),
    path('new', views.NewProduct),
    path('clearence', views.ClearenceProducts),
    path('return', views.ProductReturns)
]
