from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Blog

class BlogAdmin(ModelAdmin):
	list_display = ('title', 'author', 'status','content' , 'created_on', 'updated_on', 'slug')
	search_fields = ('title', 'author', 'status','content' , 'created_on', 'updated_on', 'slug')
	readonly_fields = ('created_on', 'updated_on',)
	filter_horizontal = ()
	list_filter = ()
	ordering = ('title',)
	fieldsets = ()

admin.site.register(Blog, BlogAdmin)
