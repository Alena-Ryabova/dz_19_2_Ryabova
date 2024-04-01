from django.urls import path

from catalog.views import IndexListView, ContactTemplateView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contact/', ContactTemplateView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product')
]
