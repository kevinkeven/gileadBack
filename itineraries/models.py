from django.db import models
from shared.models import Month, Country


class itineraries(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="itineraries",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="itineraries/images")
    price = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True)
    transport = models.CharField(max_length=100)
    accommodation = models.CharField(max_length=100)
    departureFrom = models.CharField(max_length=100)

    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Included(models.Model):
    itinerary = models.ForeignKey(itineraries, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Excluded(models.Model):
    itinerary = models.ForeignKey(itineraries, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ItineraryActivity(models.Model):
    itinerary = models.ForeignKey(itineraries, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ItineraryMonth(models.Model):
    class MoodChoices(models.TextChoices):
        BEST = "BEST"
        GOOD = "GOOD"
        MIXED = "MIXED"

    itinerary = models.ForeignKey(
        itineraries, on_delete=models.CASCADE, related_name="months"
    )
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    when_to_visit = models.CharField(max_length=6, choices=MoodChoices.choices)

    def __str__(self) -> str:
        return f" {self.itinerary} - {self.month}"


class dayByDay(models.Model):
    itinerary = models.ForeignKey(
        itineraries, on_delete=models.CASCADE, related_name="daybyday"
    )
    image = models.ImageField(upload_to="itineraries/daybyday", blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    nights = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]
