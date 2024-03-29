from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from materials.models import Blogpost


class BlogpostCreateView(CreateView):
    model = Blogpost
    fields = ('post_name', 'blog_content', 'blog_preview',)
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.post_name)
            new_post.save()

        return super().form_valid(form)


class BlogpostListView(ListView):
    model = Blogpost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_indicator=True)
        return queryset


class BlogpostDetailView(DetailView):
    model = Blogpost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()
        return self.object


class BlogpostUpdateView(UpdateView):
    model = Blogpost
    fields = ('post_name', 'blog_content', 'blog_preview',)
    success_url = reverse_lazy('materials:list')

    def get_success_url(self):
        return reverse('materials:detail', args=[self.kwargs.get('pk')])


class BlogpostDeleteView(DeleteView):
    model = Blogpost
    success_url = reverse_lazy('materials:list')
