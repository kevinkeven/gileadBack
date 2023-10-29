from rest_framework import serializers
from blog.models import Post, Category


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class BlogCreationSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Post
        exclude = ["slug"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
