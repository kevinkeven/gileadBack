from rest_framework import serializers
from enquire.models import Enquire, ContactUs


# Enquire Serializer
class EnquireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquire
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"
