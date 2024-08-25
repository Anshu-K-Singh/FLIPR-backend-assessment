from django.urls import path
from .views import AddToCartView, UpdateCartView, DeleteFromCartView, GetCartView

urlpatterns = [
    path('addtocart/', AddToCartView.as_view(), name='addtocart'),
    path('updatecart/', UpdateCartView.as_view(), name='updatecart'),
    path('deletefromcart/', DeleteFromCartView.as_view(), name='deletefromcart'),
    path('cart/', GetCartView.as_view(), name='cart'),
]
