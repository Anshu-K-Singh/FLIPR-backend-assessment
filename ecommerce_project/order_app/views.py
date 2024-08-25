from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from cart_app.models import Cart
from .serializers import OrderSerializer

class PlaceOrderView(APIView):
    def post(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items:
            return Response({"message": "Your cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        total_amount = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(user=request.user, total_amount=total_amount)
        order.cart_items.set(cart_items)
        order.save()

        cart_items.delete()  # Clear the cart after placing the order

        return Response({"message": "Order placed successfully", "order_id": order.id}, status=status.HTTP_201_CREATED)

class GetOrdersView(APIView):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        if not orders:
            return Response({"message": "No orders found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
