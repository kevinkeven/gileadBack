from rest_framework import serializers
from itineraries import models


# #Itinerary serializers
class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.itineraries
        fields = "__all__"


class ItineraryActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItineraryActivity
        fields = "__all__"


class ItineraryMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItineraryMonth
        fields = "__all__"


class IncludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Included
        fields = "__all__"


class ExcludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Excluded
        fields = "__all__"


class dayByDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.dayByDay
        fields = "__all__"
