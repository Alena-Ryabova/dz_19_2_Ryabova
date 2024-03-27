from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product


# def index(request):
#     product_all = Product.objects.all()
#     context = {
#         'object_list': product_all
#     }
#     return render(request, 'catalog/index.html', context)

class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Имя - {name}; Телефон - {phone}; Сообщение - {message};')
#     return render(request, 'catalog/contact.html')

class ContactTemplateView(TemplateView):
    template_name = 'catalog/contact.html'


# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object': product_item
#     }
#     return render(request, 'catalog/product.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
