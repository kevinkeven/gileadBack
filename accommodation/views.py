from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from rest_framework import permissions
from accommodation import serializers
from accommodation import models

from shared.serializers import WildLifeSerializer, ActivitySerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView

from rest_framework import permissions

from shared import serializers as shser
from shared import models as shmod


# Accommodation Create, List, Detail, Update, Delete views
class AccommodationList(generics.ListAPIView):
    queryset = models.Accommodation.objects.all()
    serializer_class = serializers.AccommodationSerializer


class AccommodationCreate(generics.CreateAPIView):
    queryset = models.Accommodation.objects.all()
    serializer_class = serializers.AccommodationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AccommodationDetail(generics.GenericAPIView):
    def get(self, request, slug):
        accommodation = get_object_or_404(models.Accommodation, slug=slug)
        accommodation_serializer = serializers.AccommodationSerializer(
            accommodation
        ).data
        accommodation_serializer["image"] = request.build_absolute_uri(
            accommodation.image.url
        )
        insidertip = accommodation.insidertip
        insidertip_serializer = serializers.InsiderTipSerializerDetail(insidertip)

        expertview = accommodation.expertview.all()
        expertview_serializer = serializers.ExpertViewSerializerDetail(
            expertview, many=True
        )

        glance = accommodation.glance.all()
        glance_serializer = serializers.GlanceSerializerDetail(glance, many=True)

        gallery_id = shmod.Gallery.objects.get(id=accommodation.gallery.id)

        gallery_images = gallery_id.images.all()

        gallery_serializers = shser.ImageSerializer(gallery_images, many=True).data
        for image in gallery_serializers:
            image["image"] = request.build_absolute_uri(image["image"])

        response_data = {
            "accommodation": accommodation_serializer,
            "insidertip": insidertip_serializer.data,
            "expertview": expertview_serializer.data,
            "glance": glance_serializer.data,
            "galleryImages": gallery_serializers,
        }

        return Response(response_data)


class AccommodationDestroy(generics.DestroyAPIView):
    queryset = models.Accommodation.objects.all()
    serializer_class = serializers.AccommodationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AccommodationUpdate(generics.UpdateAPIView):
    queryset = models.Accommodation.objects.all()
    serializer_class = serializers.AccommodationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AccomodationActivitiesList(generics.ListAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        destination_pk = self.kwargs.get("pk")
        return super().get_queryset()


class AccommodationListByDestination(generics.ListAPIView):
    serializer_class = serializers.AccommodationSerializer

    def get_queryset(self):
        destination_pk = self.kwargs.get("pk")
        return models.Accommodation.objects.filter(destination_id=destination_pk)


# ExpertView Create, List, Detail, Update, Delete views
class ExpertViewList(generics.ListAPIView):
    queryset = models.ExpertView.objects.all()
    serializer_class = serializers.ExpertViewSerializer


class ExpertViewListByAccommodation(generics.ListAPIView):
    serializer_class = serializers.ExpertViewSerializer

    def get_queryset(self):
        accommodation_pk = self.kwargs.get("pk")
        return models.ExpertView.objects.filter(accommodation_id=accommodation_pk)


class ExpertViewCreate(generics.CreateAPIView):
    queryset = models.ExpertView.objects.all()
    serializer_class = serializers.ExpertViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExpertViewDetail(generics.RetrieveAPIView):
    queryset = models.ExpertView.objects.all()
    serializer_class = serializers.ExpertViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExpertViewDestroy(generics.DestroyAPIView):
    queryset = models.ExpertView.objects.all()
    serializer_class = serializers.ExpertViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExpertViewUpdate(generics.UpdateAPIView):
    queryset = models.ExpertView.objects.all()
    serializer_class = serializers.ExpertViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Glance Create, List, Detail, Update, Delete views
class GlanceList(generics.ListAPIView):
    queryset = models.Glance.objects.all()
    serializer_class = serializers.GlanceSerializer


class GlanceListByAccommodation(generics.ListAPIView):
    serializer_class = serializers.GlanceSerializer

    def get_queryset(self):
        accommodation_pk = self.kwargs.get("pk")
        return models.Glance.objects.filter(accommodation_id=accommodation_pk)


class GlanceCreate(generics.CreateAPIView):
    queryset = models.Glance.objects.all()
    serializer_class = serializers.GlanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GlanceDetail(generics.RetrieveAPIView):
    queryset = models.Glance.objects.all()
    serializer_class = serializers.GlanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GlanceDestroy(generics.DestroyAPIView):
    queryset = models.Glance.objects.all()
    serializer_class = serializers.GlanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GlanceUpdate(generics.UpdateAPIView):
    queryset = models.Glance.objects.all()
    serializer_class = serializers.GlanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# InsiderTip Create, List, Detail, Update, Delete views
class InsiderTipList(generics.ListAPIView):
    queryset = models.InsiderTip.objects.all()
    serializer_class = serializers.InsiderTipSerializer


class InsiderTipCreate(generics.CreateAPIView):
    queryset = models.InsiderTip.objects.all()
    serializer_class = serializers.InsiderTipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InsiderTipDetail(generics.RetrieveAPIView):
    queryset = models.InsiderTip.objects.all()
    serializer_class = serializers.InsiderTipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InsiderTipDestroy(generics.DestroyAPIView):
    queryset = models.InsiderTip.objects.all()
    serializer_class = serializers.InsiderTipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InsiderTipUpdate(generics.UpdateAPIView):
    queryset = models.InsiderTip.objects.all()
    serializer_class = serializers.InsiderTipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InsiderTipListByAccommodation(generics.ListAPIView):
    serializer_class = serializers.InsiderTipSerializer

    def get_queryset(self):
        accommodation_pk = self.kwargs.get("pk")
        return models.InsiderTip.objects.filter(accommodation_id=accommodation_pk)


# Itinerary Create, List, Detail, Update, Delete views
