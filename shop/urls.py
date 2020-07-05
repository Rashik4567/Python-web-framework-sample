from django.contrib import admin
from django.urls import path
from . import views

app = 'shop'

urlpatterns = [
    path('<int:product_id>', views.product, name='product'),
    path('', views.Home, name='E_shop'),
]
