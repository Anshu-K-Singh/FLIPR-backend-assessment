from django.urls import path
from .views import AddProductView, UpdateProductView, DeleteProductView, GetAllProductsView

urlpatterns = [
    path('addproduct/', AddProductView.as_view(), name='addproduct'),
    path('updateproduct/<int:product_id>/', UpdateProductView.as_view(), name='updateproduct'),
    path('deleteproduct/<int:product_id>/', DeleteProductView.as_view(), name='deleteproduct'),
    path('products/', GetAllProductsView.as_view(), name='products'),
]
