from rest_framework import serializers
from accommodation import models


# ExpertView serializer
class ExpertViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpertView
        fields = "__all__"


class ExpertViewSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = models.ExpertView
        fields = ["name"]


class ExpertViewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpertView
        exclude = ("accommodation",)


# Accommodation serializer
class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Accommodation
        fields = "__all__"


class AccommodationSerializerDetailed(serializers.ModelSerializer):
    class Meta:
        model = models.Accommodation
        fields = ["name", "image"]


class AccommodationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Accommodation
        exclude = ("destination", "slug")


class GlanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Glance
        fields = "__all__"


class GlanceSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Glance
        fields = ["description"]


class GlanceSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Glance
        fields = ["description"]


# InsiderTip serializer
class InsiderTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InsiderTip
        fields = "__all__"


class InsiderTipSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = models.InsiderTip
        fields = ["description"]
