# from django.shortcuts import render
from orders.models import Order
from rest_framework import generics
from orders.serializer import OrderSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializer import BookSerializer



class OrderCreateListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
class OrderTotalPriceView(APIView):
    def get(self,request, order_number):
        try:
            order = Order.objects.get(order_number= order_number)
            # print("esse é o order: ",order)
            # cart = Order.cart
            # print("esse é o cart: ",cart)
            # book_titles = [ item['title'] for item in cart ]
            # print("esse é o titles: ",book_titles)
            return Response({"total_price":order.total_price}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"detail":"Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        
        
class BookCreateListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
