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
            order = Order.objects.get(order_number= order_number)  # pega o pedido buscado através do order_number 
            print("esse é o order: ",order)
            
            cart = order.cart                                       # cart do pedido
            print("esse é o cart: ",cart)
            
            book_titles = [ item.get('title') for item in cart ] # Titulo dos livros adicionados no cart do pedido
            print("esse é o titles: ",book_titles)
            
            sum_total_price = 0
            
            # For de titulo de livros do carrinho do Pedido 
            for book_title in book_titles:                     
                book_DB = Book.objects.get(title=book_title)   # Pega cada titulo do livro do carrinho e busca no banco de dados da APi o modelo Book,
                sum_total_price += book_DB.total_value         # Pega o valor de cada titulo do livro do carrinho e busca no banco de dados do modelo Book
                print("Esse é o book DB: ",book_DB)
                print("Esse é o sum_total_price: ",sum_total_price)

            # return Response({"total_price":order.total_price}, status=status.HTTP_200_OK) # Método anterior somando o valor dos livros que o usuario mandou (VALOR QUE O USUARIO MANDOU)
            return Response({"total_price":sum_total_price}, status=status.HTTP_200_OK) # Novo método que soma os valores cadastrados no banco de dados da API (VALOR CADASTRADO NA API)
        except Order.DoesNotExist:
            return Response({"detail":"Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        
        
class BookCreateListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
