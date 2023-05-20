# # Image serializers
from rest_framework import serializers
from shared import models


# #Image serializers
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields = "__all__"


class ImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        exclude = ("id", "created_at")


# #Country serializers
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"


class CountryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        exclude = ("slug", "id")


# #Activity serializers
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = "__all__"


class ActivityUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        exclude = "id"


# #Wildlife serializers
class WildLifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wildlife
        fields = "__all__"


class WildLifeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wildlife
        exclude = "id"


# #Gallery serializers
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = "__all__"


class GalleryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        exclude = "id"
