from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from shared import serializers
from destination.serializers import DestinationSerializer
from destination.models import Destination
from itineraries.serializers import ItinerarySerializer
from shared import models
from rest_framework import permissions


# Images Create, List, Detail, Update, Delete views
class ImageList(generics.ListAPIView):
    queryset = models.Images.objects.all()
    serializer_class = serializers.ImageSerializer


class ImageCreate(generics.CreateAPIView):
    queryset = models.Images.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImageDetailDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Images.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImageUpdate(generics.UpdateAPIView):
    queryset = models.Images.objects.all()
    serializer_class = serializers.ImageUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Country Create, List, Detail, Update, Delete views
class CountryList(generics.ListAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CountryDetail(generics.GenericAPIView):
    def get(self, request, slug):
        country = get_object_or_404(models.Country, slug=slug)
        country_serializer = serializers.CountrySerializer(country).data
        country_serializer["image"] = request.build_absolute_uri(country.image.url)

        destinations = country.destinations.all()
        destinations_serializer = DestinationSerializer(destinations, many=True).data

        for destination in destinations_serializer:
            destination["image"] = request.build_absolute_uri(destination["image"])

        countryMonth = country.months.all()
        countryMonth_serializer = serializers.CountryMonthSerializer(
            countryMonth, many=True
        ).data

        countryfamousof = country.famousof.all()
        countryfamousof_serializer = serializers.CountryFamousForSerializer(
            countryfamousof, many=True
        ).data

        countryhomeFor = country.homeof.all()
        countryhomeFor_serializer = serializers.countryHomeOfferSerializer(
            countryhomeFor, many=True
        ).data

        itineraries = country.itineraries.all()
        itineraryserializer = ItinerarySerializer(itineraries, many=True).data
        for itinerary in itineraryserializer:
            itinerary["image"] = request.build_absolute_uri(itinerary["image"])

        gallery_id = models.Gallery.objects.get(id=country.gallery.id)

        gallery_images = gallery_id.images.all()

        gallery_serializers = serializers.ImageSerializer(
            gallery_images, many=True
        ).data
        for image in gallery_serializers:
            image["image"] = request.build_absolute_uri(image["image"])

        response = {
            "country": country_serializer,
            "destinations": destinations_serializer,
            "countryMonth": countryMonth_serializer,
            "countryfamousof": countryfamousof_serializer,
            "countryhomeFor": countryhomeFor_serializer,
            "itineraries": itineraryserializer,
            "galleryImages": gallery_serializers,
        }
        return Response(response)


class CountryDestinations(generics.RetrieveAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CountryDestroy(generics.DestroyAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CountryCreate(generics.CreateAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CountryDestinationsList(generics.ListAPIView):
    serializer_class = DestinationSerializer

    def get_queryset(self):
        country_id = self.kwargs["pk"]
        country = models.Country.objects.get(pk=country_id)
        destination_ids = country.destinations.all().values_list("id", flat=True)
        queryset = Destination.objects.filter(id__in=destination_ids)
        return queryset


class CountryUpdate(generics.UpdateAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountryUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Activity Create, List, Detail, Update, Delete views
class ActivityList(generics.ListAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer


class ActivityCreate(generics.CreateAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ActivityDetailDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ActivityUpdate(generics.UpdateAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivityUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ActivityDestinationsList(generics.ListAPIView):
    seriliazer_class = DestinationSerializer

    def get_queryset(self):
        activity_id = self.kwargs["pk"]
        activity = models.Activity.objects.get(pk=activity_id)
        destination_ids = activity.destinations.all().values_list("id", flat=True)
        queryset = Destination.objects.filter(id__in=destination_ids)
        return queryset


# WildLife Create, List, Detail, Update, Delete views
class WildlifeList(generics.ListAPIView):
    queryset = models.Wildlife.objects.all()
    serializer_class = serializers.WildLifeSerializer


class WildlifeCreate(generics.CreateAPIView):
    queryset = models.Wildlife.objects.all()
    serializer_class = serializers.WildLifeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WildlifeDetailDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Wildlife.objects.all()
    serializer_class = serializers.WildLifeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WildlifeUpdate(generics.UpdateAPIView):
    queryset = models.Wildlife.objects.all()
    serializer_class = serializers.WildLifeUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# GALLERY Create, List, Detail, Update, Delete views
class GalleryList(generics.ListAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer


class GalleryImageList(generics.ListAPIView):
    serializer_class = serializers.ImageSerializer

    def get_queryset(self):
        gallery_id = self.kwargs["pk"]
        gallery = models.Gallery.objects.get(pk=gallery_id)
        image_ids = gallery.images.all().values_list("id", flat=True)
        queryset = models.Images.objects.filter(id__in=image_ids)
        return queryset


class GalleryDetail(generics.RetrieveAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer


class GalleryCreate(generics.CreateAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GalleryUpdate(generics.UpdateAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GalleryDestroy(generics.DestroyAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
