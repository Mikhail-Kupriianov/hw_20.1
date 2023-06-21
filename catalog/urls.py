from django.urls import path

from blog.views import BlogListView
from catalog.views import ProductListView, contact, ProductCreateView, ProductUpdateView  # MessageSend


from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contact, name='contacts'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    # path('contacts/', MessageSend.as_view(), name='contacts'),
]
