from django.urls import path
from .api import BlogApi, BlogCreateApi, BlogDetailApi

app_name = 'blog_api'

urlpatterns = [
	path('', BlogApi.as_view(), name='blogs'),
	path('create', BlogCreateApi.as_view(), name='blog_create'),
	path('<slug:slug>', BlogDetailApi.as_view(), name='blog_detail'),

]
