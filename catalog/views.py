from django.shortcuts import render

from catalog.models import Product


def index(request):
    product_all = Product.objects.all()
    context = {
        'object_list': product_all
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя - {name}; Телефон - {phone}; Сообщение - {message};')
    return render(request, 'catalog/contact.html')


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': product_item
    }
    return render(request, 'catalog/product.html', context)
