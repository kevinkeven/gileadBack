from rest_framework import serializers
from enquire.models import Enquire


# Enquire Serializer
class EnquireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquire
        fields = "__all__"
