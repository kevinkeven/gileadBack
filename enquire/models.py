from django.db import models
from shared.models import Country
import uuid

# Create your models here.


class Enquire(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    itinerary = models.ForeignKey(
        "itineraries.itineraries",
        on_delete=models.CASCADE,
        related_name="enquiries",
        blank=True,
        null=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class TRAVEL_TYPE(models.TextChoices):
        LUXURY = "Luxury"
        MIDRANGE = "Midrange"
        BUDGET = "Budget"

    travel_destination = models.ManyToManyField(
        Country, related_name="yourtrip", blank=True
    )
    travel_date = models.DateField()
    travel_duration = models.IntegerField()
    travel_type = models.CharField(
        max_length=10, choices=TRAVEL_TYPE.choices, default=TRAVEL_TYPE.MIDRANGE
    )
    adults = models.IntegerField(default=0)
    children = models.IntegerField(default=0, blank=True, null=True)
    special_request = models.TextField()

    def __str__(self):
        return f"Enquiry from {self.first_name} {self.last_name} - {self.travel_destination.name}"

    class Meta:
        verbose_name_plural = "Enquiries"


class ContactUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"Contact from {self.first_name} {self.last_name} - {self.message}"

    class Meta:
        verbose_name_plural = "Contact Us"
