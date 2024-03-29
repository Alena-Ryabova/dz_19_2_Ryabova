from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import BlogpostCreateView, BlogpostListView, BlogpostDetailView, BlogpostUpdateView, \
    BlogpostDeleteView

app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', BlogpostCreateView.as_view(), name='create'),
    path('list/', BlogpostListView.as_view(), name='list'),
    path('edit/<int:pk>/', BlogpostUpdateView.as_view(), name='edit'),
    path('detail/<int:pk>/', BlogpostDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BlogpostDeleteView.as_view(), name='delete'),

]
