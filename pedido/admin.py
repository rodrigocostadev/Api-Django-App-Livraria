from django.contrib import admin
from pedido.models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('order_number','username')

