from django.db import models


class Order(models.Model):
    
    # Número do Pedido
    order_number = models.IntegerField()
    
    # Usuario
    user_id = models.IntegerField() # Talvez colocar / Falta enviar por formulário no projeto
    user_name = models.CharField(max_length=200) # Falta enviar por formulário no projeto
    first_name = models.CharField(max_length=150) # Falta enviar por formulário no projeto
    last_name = models.CharField(max_length=150) # Falta enviar por formulário no projeto

    # Livro
    book_title = models.CharField(max_length=150)
    book_price = models.FloatField()
    book_quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Endereço
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    house_number = models.IntegerField()
    cep = models.IntegerField()
    
    # Dados Pagamento
    payment_method = models.CharField(max_length=200)
    card_name = models.CharField(max_length=200)
    card_number = models.IntegerField()
    card_security_code = models.IntegerField()
    card_validity_month = models.IntegerField()
    card_validity_year = models.IntegerField()
    
    # Data de criação do pedido
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    # def saveTotalPrice(self, *args, **kwargs):
    #     self.total_price = self.book_price * self.book_quantity
    #     super().save(*args, **kwargs)

    
    def __str__(self):
        return f"Pedido {self.order_number} para {self.user_name} criado no dia: {self.created_at}"

