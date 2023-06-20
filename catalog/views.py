from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    paginate_by = 4
    model = Product
    extra_context = {
        'title': 'Главная'
    }


# Create your views here.
# def index(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/home.html', context, )

# def send(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'You have new message from {name}({phone}): {message}')
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'catalog/contacts.html', context)


# class MessageSend(TemplateView):
#     template_name = 'catalog/message_send.html'  # Шаблоны
#     # fields = ('blog_title', 'blog_content', 'blog_preview', 'blog_is_publicated')
#     MessageSend.request.
#     success_url = reverse_lazy('catalog:index')

    # def send(self, request):
    #     if request.method == 'POST':
    #         name = request.POST.get('name')
    #         phone = request.POST.get('phone')
    #         message = request.POST.get('message')
    #         print(f'You have new message from {name}({phone}): {message}')
    #     context = {
    #         'title': 'Контакты'
    #     }
    #     return render(request, 'catalog/contacts.html', context)

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
