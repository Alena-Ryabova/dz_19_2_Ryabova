from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import Http404, HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        current_user = self.request.user
        if current_user.is_superuser:
            return queryset
        else:
            return queryset.filter(owner=current_user)


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'
    permission_required = 'catalog.view_product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if (
                self.object.owner != self.request.user
                or self.request.user.is_superuser is True
                or self.request.user.groups.filter(name="moderators").exists() is True
        ):
            return self.object
        raise Http404

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        print("Debug: Form is valid")
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            for form in formset.forms:
                if form.instance:
                    form.instance.version_indicator = True
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class ProductModeratorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductModeratorForm
    template_name = 'catalog/product_form.html'
    reverse_lazy = 'catalog/product_form.html'

    def test_func(self):
        # Проверяем, является ли текущий пользователь модератором
        return self.request.user.groups.filter(name="moderators").exists()

    def handle_no_permission(self):
        # Возвращаем статус код 403 Forbidden, если у пользователя нет доступа
        return HttpResponseForbidden()

    # def get_success_url(self):
    #     return reverse('catalog:product', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        return self.request.user.is_superuser


class ContactTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/contact.html'
