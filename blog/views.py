from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from blog.serializers import BlogSerializer, CategorySerializer, BlogCreationSerializers
from rest_framework import generics


# Create your views here.
class BlogList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class BlogCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogCreationSerializers


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
