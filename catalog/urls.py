from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ContactTemplateView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductListView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contact/', ContactTemplateView.as_view()),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
