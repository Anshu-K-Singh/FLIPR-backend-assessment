from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializers import CartSerializer

class AddToCartView(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            cart_item, created = Cart.objects.update_or_create(
                user=request.user,
                product=serializer.validated_data['product'],
                defaults={'quantity': serializer.validated_data['quantity']}
            )
            return Response({"message": "Product added to cart", "cart_id": cart_item.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCartView(APIView):
    def put(self, request):
        try:
            cart_item = Cart.objects.get(user=request.user, product=request.data['product'])
            cart_item.quantity = request.data['quantity']
            cart_item.save()
            return Response({"message": "Cart updated successfully"}, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"error": "Product not found in cart"}, status=status.HTTP_404_NOT_FOUND)

class DeleteFromCartView(APIView):
    def delete(self, request):
        try:
            cart_item = Cart.objects.get(user=request.user, product=request.data['product'])
            cart_item.delete()
            return Response({"message": "Product removed from cart"}, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"error": "Product not found in cart"}, status=status.HTTP_404_NOT_FOUND)

class GetCartView(APIView):
    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items:
            return Response({"message": "Your cart is empty"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
