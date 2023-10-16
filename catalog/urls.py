from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, product, product_item

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', product, name='product'),
    path('product/<int:pk>/', product_item, name='product_item'),
]
