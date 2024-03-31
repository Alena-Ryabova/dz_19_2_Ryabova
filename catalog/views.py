from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:update_product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(*kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
