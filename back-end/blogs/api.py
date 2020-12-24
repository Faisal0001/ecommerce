from rest_framework.response import Response
from rest_framework.serializers import Serializer
from blogs.models import Blog
from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView)
from .serializers import BlogSerializer, BlogDetailSerializer

class BlogApi(ListAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer


class BlogDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field =  'slug'

class BlogCreateApi(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        author = self.request.user
        serializer = serializer.save(author=author)
        return Response(serializer)
