from django.urls import path

from catalog.views import IndexListView, ContactTemplateView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contact/', ContactTemplateView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product')
]
