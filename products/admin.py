from django.contrib import admin
from .models import Product, Order, OrderProduct, Cart
from django.contrib.admin import ModelAdmin


class ProductAdmin(ModelAdmin):
	list_display = ('name', 'discount_price', 'price' , 'description')
	search_fields =  ('name', 'discount_price', 'price' , 'description')
	filter_horizontal = ()
	list_filter = ()
	ordering = ('name',)
	fieldsets = ()

class OrderProductAdmin(ModelAdmin):
	list_display = ('product', 'quantity', 'user' , 'ordered')
	search_fields =  ('product', 'quantity', 'user' , 'ordered')
	filter_horizontal = ()
	list_filter = ()
	ordering = ('product',)
	fieldsets = ()

class OrderAdmin(ModelAdmin):
	list_display = ('user', 'get_products', 'ordered','start_date' , 'ordered_date')
	search_fields =  ('user', 'get_products', 'ordered','start_date' , 'ordered_date')
	filter_horizontal = ()
	list_filter = ()
	ordering = ('user',)
	fieldsets = ()


admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)

