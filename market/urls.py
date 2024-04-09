from django.urls import path

from market.views import get_products, get_product

urlpatterns = [
    path('products/', get_products, name='get_products'),
    path('products/<int:product_id>/', get_product, name='get_product')
]