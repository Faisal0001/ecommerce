from django.urls import path
from .api import ProductsApi, CartApi

app_name = 'products_api'


urlpatterns = [
	path('', ProductsApi.as_view(), name='products'),
	path('cart', CartApi.as_view(), name='cart')

]

