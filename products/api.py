import django
from rest_framework import serializers
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import ProductSerializer, CartSerializer
from .models import Product, Cart




class ProductsApi(generics.ListAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()


class CartApi(generics.ListAPIView):
	serializer_class = CartSerializer

	def get_queryset(self, *args, **kwargs):
		return self.request.user.cart

