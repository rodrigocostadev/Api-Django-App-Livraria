from django.db import models


class Order(models.Model):
    
    # Número do Pedido
    order_number = models.IntegerField(blank=True, null=True)
    
    # Usuario
    user_id = models.IntegerField() # Talvez colocar / Falta enviar por formulário no projeto
    user_name = models.CharField(max_length=200) # Falta enviar por formulário no projeto
    first_name = models.CharField(max_length=150) # Falta enviar por formulário no projeto
    last_name = models.CharField(max_length=150) # Falta enviar por formulário no projeto

    # Livro
    # book_title = models.CharField(max_length=150)
    # book_price = models.FloatField()
    # book_quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    
    # Carrinho
    cart = models.JSONField()

    # Endereço
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    house_number = models.IntegerField()
    cep = models.IntegerField()
    
    # Dados Pagamento
    payment_method = models.CharField(max_length=200)
    card_name = models.CharField(max_length=200,blank=True, null=True)
    card_number = models.IntegerField(blank=True, null=True)
    card_security_code = models.IntegerField(blank=True, null=True)
    card_validity_month = models.IntegerField(blank=True, null=True)
    card_validity_year = models.IntegerField(blank=True, null=True)
    
    # Data de criação do pedido
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        
        # ID vai ser igual ao numero do pedido ( NÃO DEU CERTO POIS O ID É INCLUÍDO APÓS OS DADOS TEREM SIDO SALVOS ) 
        # if not self.order_number:
            #self.order_number = self.id

        # Soma os itens do carrinho para dar o valor total 
        if self.cart:
            self.total_price = sum(item['totalValue'] for item in self.cart)
            
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f"Pedido {self.order_number} para o usuario {self.user_name} feito no dia: {self.created_at}"
    
    
    
    
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

