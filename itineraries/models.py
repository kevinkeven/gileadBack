from django.db import models
from shared.models import Month

# Create your models here.


class itineraries(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="/itineraries")
    price = models.IntegerField()
    duration = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True)
    transport = models.CharField(max_length=100)
    accommodation = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name


class Included(models.Model):
    name = models.CharField(max_length=100)
    itinerary = models.ForeignKey(itineraries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Excluded(models.Model):
    name = models.CharField(max_length=100)
    itinerary = models.ForeignKey(itineraries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ItineraryActivity(models.Model):
    itinerary = models.ForeignKey(itineraries, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ItineraryMonth(models.Model):
    itinerary = models.ForeignKey(itineraries, on_delete=models.CASCADE)

    class MoodChoices(models.TextChoices):
        BEST = "BEST"
        GOOD = "GOOD"
        MIXED = "MIXED"

    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    when_to_visit = models.CharField(max_length=6, choices=MoodChoices.choices)

    def __str__(self) -> str:
        return f" {self.itineraries} - {self.month}"


class ItineraryLocation(models.Model):
    itinerary = models.ForeignKey(itineraries, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


# class ItineraryMonth(models.Mo)
