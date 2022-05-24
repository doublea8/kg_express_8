from django.urls import path
from .views import *


urlpatterns = [
    path('add/<int:pk>/', AddCartView.as_view(), name='add_cart'),
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('remove/<int:pk>/', RemoveCartView.as_view(), name='remove_cart'),
    path('clear/', ClearCartView.as_view(), name='clear_cart')
]