from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from itineraries import serializers
from itineraries import models
from shared import models as shared_models
from shared import serializers as shared_serializers

from rest_framework import permissions


# Itinerary views
class ItineraryList(generics.ListAPIView):
    queryset = models.itineraries.objects.all()
    serializer_class = serializers.ItinerarySerializer


class ItineraryCreate(generics.CreateAPIView):
    queryset = models.itineraries.objects.all()
    serializer_class = serializers.ItinerarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ItineraryDetail(generics.GenericAPIView):
    def get(self, request, slug):
        itinerary = get_object_or_404(models.itineraries, slug=slug)
        itinerary_serializer = serializers.ItinerarySerializer(itinerary).data

        itinerarymonth = models.ItineraryMonth.objects.filter(itinerary_id=itinerary.id)
        itinerarymonth_serializer = serializers.ItineraryMonthSerializer(
            itinerarymonth, many=True
        ).data

        itineraryactivity = models.ItineraryActivity.objects.filter(
            itinerary_id=itinerary.id
        )
        itineraryactivity_serializer = serializers.ItineraryActivitySerializer(
            itineraryactivity, many=True
        ).data

        included = models.Included.objects.filter(itinerary_id=itinerary.id)
        included_serializer = serializers.IncludedSerializer(included, many=True).data

        excluded = models.Excluded.objects.filter(itinerary_id=itinerary.id)
        excluded_serializer = serializers.ExcludedSerializer(excluded, many=True).data

        daybyday = models.dayByDay.objects.filter(itinerary_id=itinerary.id)
        daybyday_serializer = serializers.dayByDaySerializer(daybyday, many=True).data

        itinerary_serializer["image"] = request.build_absolute_uri(
            itinerary_serializer["image"]
        )

        for daybydayImage in daybyday_serializer:
            daybydayImage["image"] = request.build_absolute_uri(daybydayImage["image"])

        respone = {
            "itinerary": itinerary_serializer,
            "itinerarymonth": itinerarymonth_serializer,
            "itineraryactivity": itineraryactivity_serializer,
            "included": included_serializer,
            "excluded": excluded_serializer,
            "daybyday": daybyday_serializer,
        }

        return Response(respone)


class ItineraryUpdate(generics.UpdateAPIView):
    queryset = models.itineraries.objects.all()
    serializer_class = serializers.ItinerarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ItineraryDelete(generics.DestroyAPIView):
    queryset = models.itineraries.objects.all()
    serializer_class = serializers.ItinerarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ItineraryActivity views
class ItineraryActivityList(generics.ListAPIView):
    queryset = models.ItineraryActivity.objects.all()
    serializer_class = serializers.ItineraryActivitySerializer


class ItineraryActivityCreate(generics.CreateAPIView):
    queryset = models.ItineraryActivity.objects.all()
    serializer_class = serializers.ItineraryActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ItineraryActivityDetail(generics.RetrieveAPIView):
    queryset = models.ItineraryActivity.objects.all()
    serializer_class = serializers.ItineraryActivitySerializer


class ItineraryActivityUpdate(generics.UpdateAPIView):
    queryset = models.ItineraryActivity.objects.all()
    serializer_class = serializers.ItineraryActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ItineraryActivityDelete(generics.DestroyAPIView):
    queryset = models.ItineraryActivity.objects.all()
    serializer_class = serializers.ItineraryActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ItineraryMonth views
class ItineraryMonthList(generics.ListAPIView):
    queryset = models.ItineraryMonth.objects.all()
    serializer_class = serializers.ItineraryMonthSerializer


class ItineraryMonthCreate(generics.CreateAPIView):
    queryset = models.ItineraryMonth.objects.all()
    serializer_class = serializers.ItineraryMonthSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ItineraryMonthDetail(generics.RetrieveAPIView):
    queryset = models.ItineraryMonth.objects.all()
    serializer_class = serializers.ItineraryMonthSerializer


class ItineraryMonthUpdate(generics.UpdateAPIView):
    queryset = models.ItineraryMonth.objects.all()
    serializer_class = serializers.ItineraryMonthSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ItineraryMonthDelete(generics.DestroyAPIView):
    queryset = models.ItineraryMonth.objects.all()
    serializer_class = serializers.ItineraryMonthSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Included views
class IncludedList(generics.ListAPIView):
    queryset = models.Included.objects.all()
    serializer_class = serializers.IncludedSerializer


class IncludedCreate(generics.CreateAPIView):
    queryset = models.Included.objects.all()
    serializer_class = serializers.IncludedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IncludedDetail(generics.RetrieveAPIView):
    queryset = models.Included.objects.all()
    serializer_class = serializers.IncludedSerializer


class IncludedUpdate(generics.UpdateAPIView):
    queryset = models.Included.objects.all()
    serializer_class = serializers.IncludedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IncludedDelete(generics.DestroyAPIView):
    queryset = models.Included.objects.all()
    serializer_class = serializers.IncludedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Excluded views
class ExcludedList(generics.ListAPIView):
    queryset = models.Excluded.objects.all()
    serializer_class = serializers.ExcludedSerializer


class ExcludedCreate(generics.CreateAPIView):
    queryset = models.Excluded.objects.all()
    serializer_class = serializers.ExcludedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExcludedDetail(generics.RetrieveAPIView):
    queryset = models.Excluded.objects.all()
    serializer_class = serializers.ExcludedSerializer


class ExcludedUpdate(generics.UpdateAPIView):
    queryset = models.Excluded.objects.all()
    serializer_class = serializers.ExcludedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExcludedDelete(generics.DestroyAPIView):
    queryset = models.Excluded.objects.all()
    serializer_class = serializers.ExcludedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# dayByDay views
class dayByDayList(generics.ListAPIView):
    queryset = models.dayByDay.objects.all()
    serializer_class = serializers.dayByDaySerializer


class dayByDayCreate(generics.CreateAPIView):
    queryset = models.dayByDay.objects.all()
    serializer_class = serializers.dayByDaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class dayByDayDetail(generics.RetrieveAPIView):
    queryset = models.dayByDay.objects.all()
    serializer_class = serializers.dayByDaySerializer


class dayByDayUpdate(generics.UpdateAPIView):
    queryset = models.dayByDay.objects.all()
    serializer_class = serializers.dayByDaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class dayByDayDelete(generics.DestroyAPIView):
    queryset = models.dayByDay.objects.all()
    serializer_class = serializers.dayByDaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
