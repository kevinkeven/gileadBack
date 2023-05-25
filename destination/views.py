from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from destination import serializers
from destination import models
from drf_multiple_model.views import ObjectMultipleModelAPIView
from accommodation import serializers as acser
from accommodation import models as acmod


# Destination Create, List, Detail, Update, Delete views
class DestinationList(generics.ListAPIView):
    queryset = models.Destination.objects.all()
    serializer_class = serializers.DestinationSerializer


class DestinationCreate(generics.CreateAPIView):
    queryset = models.Destination.objects.all()
    serializer_class = serializers.DestinationSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DestinationDetail(generics.GenericAPIView):
    def get(self, request, slug):
        destination = get_object_or_404(models.Destination, slug=slug)
        destination_serializer = serializers.DestinationSerializer(destination).data
        destination_serializer["image"] = request.build_absolute_uri(
            destination.image.url
        )
        highlights = destination.highlights.all()
        highlights_serializer = serializers.HighlightListSerializer(
            highlights, many=True
        )
        location = destination.location.all()
        location_serializer = serializers.DestinationLocationSerilializer(
            location, many=True
        )

        animalsoverview = destination.animalsoverview.all()
        animalsoverview_serializer = serializers.DestinationAnimalsOverviewSerilializer(
            animalsoverview, many=True
        )

        destinationmonth = models.DestinationMonth.objects.filter(
            destination_id=destination.id
        )
        destinationmonth_serializer = serializers.DestinationMonthSerilializer(
            destinationmonth, many=True
        ).data

        accommodation = destination.accommodations.all()
        accommodation_serializer = acser.AccommodationSerializer(
            accommodation, many=True
        ).data

        for accommodation_obj in accommodation_serializer:
            accommodation_obj["image"] = request.build_absolute_uri(
                accommodation_obj["image"]
            )

        response_data = {
            "destination": destination_serializer,
            "highlights": highlights_serializer.data,
            "location": location_serializer.data,
            "animals": animalsoverview_serializer.data,
            "destinationmonth": destinationmonth_serializer,
            "accommodations": accommodation_serializer,
        }

        return Response(response_data)


class DestinationDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Destination.objects.all()
    serializer_class = serializers.DestinationSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DestinationUpdate(generics.UpdateAPIView):
    queryset = models.Destination.objects.all()
    serializer_class = serializers.DestinationSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Highlight Create, List, Detail, Update, Delete views
class HighlightsList(generics.ListAPIView):
    queryset = models.Highlights.objects.all()
    serializer_class = serializers.HighlightSerializer


class HighlightsCreate(generics.CreateAPIView):
    queryset = models.Highlights.objects.all()
    serializer_class = serializers.HighlightSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HighlightsDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Highlights.objects.all()
    serializer_class = serializers.HighlightSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HighlightsDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Highlights.objects.all()
    serializer_class = serializers.HighlightSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HighlightsListByDestination(generics.ListAPIView):
    queryset = models.Highlights.objects.all()
    serializer_class = serializers.HighlightSerializer

    def get_queryset(self):
        dest_pk = self.kwargs.get("pk")
        return self.queryset.filter(destination_id=dest_pk)


class HighlightsUpdate(generics.UpdateAPIView):
    queryset = models.Highlights.objects.all()
    serializer_class = serializers.HighlightSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
