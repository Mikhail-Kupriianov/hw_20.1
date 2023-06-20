from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogListView(ListView):
    paginate_by = 4
    model = Blog
    extra_context = {
        'title': 'Блоги'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(blog_is_publicated=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = context_data['object']
        return context_data

    def get_object(self, queryset=None):

        post = super().get_object()
        post.inc_view_count()
        post.save()

        return post


class BlogCreateView(CreateView):
    model = Blog
    fields = ('blog_title', 'blog_content',)
    success_url = reverse_lazy('blog:blogs')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_preview', 'blog_is_publicated')

    def get_success_url(self):
        return reverse('blog:blogs_item', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blogs')
