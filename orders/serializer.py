from rest_framework import serializers
from orders.models import Order, Book

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order       
        fields = '__all__'
        
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','total_value']