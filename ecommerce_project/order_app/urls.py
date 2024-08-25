from django.urls import path
from .views import PlaceOrderView, GetOrdersView

urlpatterns = [
    path('placeorder/', PlaceOrderView.as_view(), name='placeorder'),
    path('orders/', GetOrdersView.as_view(), name='orders'),
]
