from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderCreateListView.as_view(), name="order-create-list"),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail-view'),
    path('order/total-price/<int:order_number>/', views.OrderTotalPriceView.as_view(), name='order-total-price'),
]