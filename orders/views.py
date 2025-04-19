# from django.shortcuts import render
from orders.models import Order
from rest_framework import generics
from orders.serializer import OrderSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializer import BookSerializer
from decimal import Decimal



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
            # print("esse é o order: ",order)            
            promo_code = order.promo_code                          # Verifica se há cupom de desconto
            # print("esse é o promo_code: ", promo_code )            
            cart = order.cart                                       # cart do pedido
            # print("esse é o cart: ",cart)            
            # book_titles = [ item.get('title') for item in cart ] # Titulo dos livros adicionados no cart do pedido
            # print("esse é o titles: ",book_titles)    

            sum_total_price = 0
            
            codes = [{"GANHEI5":0.05},{"APP10":0.1},{"LIVRO15":0.15},]
            
            value_code = None
            
            for item_codes in codes:
                for key, value in item_codes.items():
                   if promo_code == key:
                       value_code = value
                       
            print("Esse é o value code: ", value_code)
            
            if value_code is not None :                
                value_code = Decimal(value_code)

                # Adiciona o desconto do cupom
                for item in cart:
                    # title = item.get('title')
                    quantity = int(item.get('quantity'))
                    value_unit_book = Decimal(item.get('valueUnitBook'))
                    sum_total_price += ((value_unit_book * quantity) - ((value_unit_book * quantity) * value_code ) ) # Pega o valor de cada livro com desconto, multiplica pela quantidade e adiciona ao preço total do pedido


            else:
                # Sem cupom de desconto
                for item in cart:
                    # title = item.get('title')
                    quantity = int(item.get('quantity'))
                    value_unit_book = Decimal(item.get('valueUnitBook'))
                    sum_total_price += (value_unit_book * quantity ) # Pega o valor de cada livro, multiplica pela quantidade e adiciona ao preço total do pedido

                
                        

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











# For de titulo de livros do carrinho do Pedido 
            # for book_title in book_titles:                     
            #     book_DB = Book.objects.get(title=book_title)   # Pega cada titulo do livro do carrinho e busca no banco de dados da APi o modelo Book,
            #     sum_total_price += book_DB.total_value         # Pega o valor de cada titulo do livro do carrinho e busca no banco de dados do modelo Book
            #     print("Esse é o book DB: ",book_DB)
            #     print("Esse é o sum_total_price: ",sum_total_price)








            # Adiciona o desconto do cupom
                # for book_title in book_titles: 
                #     print("TESTE: ", book_title)                    
                #     book_DB = Book.objects.get(title=book_title)   # Pega cada titulo do livro do carrinho e busca no banco de dados da APi o modelo Book,
                #     sum_total_price += (book_DB.total_value - (book_DB.total_value * value_code ) ) 
                #     # print("Esse é o book DB: ",book_DB)
                #     # print("Esse é o sum_total_price com CUPOM: ",sum_total_price)



            # for book_title in book_titles:    
                #     print("TESTE: ", book_title)                  
                #     book_DB = Book.objects.get(title=book_title)   # Pega cada titulo do livro do carrinho e busca no banco de dados da APi o modelo Book,
                #     sum_total_price += book_DB.total_value         # Pega o valor de cada titulo do livro do carrinho e busca no banco de dados do modelo Book
                #     # print("Esse é o book DB: ",book_DB)
                #     # print("Esse é o sum_total_price: ",sum_total_price)