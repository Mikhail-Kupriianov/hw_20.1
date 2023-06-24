from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(ListView):
    paginate_by = 4
    model = Product
    extra_context = {
        'title': 'Главная'
    }

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
    #     context_data['formset'] = VersionFormset()
    #     return context_data

    # def form_valid(self, form):
    #     formset = self.get_context_data()['formset']
    #     self.object = form.save()
    #     if formset.is_valid():
    #         formset.instance = self.object
    #         formset.save()
    #
    #     return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = context_data['object']
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
