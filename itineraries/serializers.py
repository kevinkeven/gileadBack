from rest_framework import serializers
from itineraries import models
from shared import serializers as shared_serializers


# #Itinerary serializers
class ItinerarySerializer(serializers.ModelSerializer):
    country = shared_serializers.CountryShortSerializer(read_only=True)

    class Meta:
        model = models.itineraries
        fields = (
            "id",
            "name",
            "description",
            "image",
            "price",
            "duration",
            "slug",
            "transport",
            "accommodation",
            "departureFrom",
            "latitude",
            "longitude",
            "country",
        )


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
