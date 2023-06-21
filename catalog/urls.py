from django.urls import path

from catalog.views import ProductListView, contact, ProductCreateView, ProductUpdateView, \
    ProductDetailView, ProductDeleteView  # MessageSend


from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contact, name='contacts'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('product/product_item/<int:pk>', ProductDetailView.as_view(), name='product_item'),
    path('product/product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    # path('contacts/', MessageSend.as_view(), name='contacts'),
]
