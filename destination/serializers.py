from rest_framework import serializers
from destination import models


# #Destination serializers
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Destination
        fields = "__all__"


class DestinationLocationSerilializer(serializers.ModelSerializer):
    class Meta:
        model = models.DestinationLocation
        fields = "__all__"


class DestinationAnimalsOverviewSerilializer(serializers.ModelSerializer):
    class Meta:
        model = models.DestinationAnimalsOverview
        fields = "__all__"


class DestinationMonthSerilializer(serializers.ModelSerializer):
    class Meta:
        model = models.DestinationMonth
        fields = "__all__"


# # Highlight serializers
class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Highlights
        fields = "__all__"


class HighlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Highlights
        fields = ["highlight_title"]


class DestinationMonthSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.DestinationMonth
        fields = "__all__"
