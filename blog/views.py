from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from blog.serializers import BlogSerializer, CategorySerializer, BlogCreationSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
class BlogList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class BlogCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogCreationSerializers

    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    
class BlogEdit(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Post.objects.all()
    serializer_class = BlogCreationSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
