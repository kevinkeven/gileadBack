from django.shortcuts import render
from rest_framework import generics
from shared import serializers
from destination.serializers import DestinationSerializer
from destination.models import Destination
from shared import models


# Images Create, List, Detail, Update, Delete views
class ImageList(generics.ListAPIView):
    queryset = models.Images.objects.all()
    serializer_class = serializers.ImageSerializer


class ImageCreate(generics.CreateAPIView):
    queryset = models.Images.objects.all()
    serializer_class = serializers.ImageSerializer


class ImageDetailDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Images.objects.all()
    serializer_class = serializers.ImageSerializer


class ImageUpdate(generics.UpdateAPIView):
    queryset = models.Images.objects.all()
    serializer_class = serializers.ImageUpdateSerializer


# Country Create, List, Detail, Update, Delete views
class CountryList(generics.ListAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CountryCreate(generics.CreateAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CountryDestroy(generics.DestroyAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CountryDetail(generics.RetrieveAPIView):
    lookup_field = 'pk'

    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


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
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Activity Create, List, Detail, Update, Delete views
class ActivityList(generics.ListAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer


class ActivityCreate(generics.CreateAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer


class ActivityDetailDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer


class ActivityUpdate(generics.UpdateAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivityUpdateSerializer


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


class WildlifeDetailDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Wildlife.objects.all()
    serializer_class = serializers.WildLifeSerializer


class WildlifeUpdate(generics.UpdateAPIView):
    queryset = models.Wildlife.objects.all()
    serializer_class = serializers.WildLifeUpdateSerializer


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


class GalleryUpdate(generics.UpdateAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer


class GalleryDestroy(generics.DestroyAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer
