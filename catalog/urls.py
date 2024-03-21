from django.urls import path

from catalog.views import index, contact, product

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact),
    path('product/<int:pk>', product, name='product')
]
