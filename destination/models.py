from django.db import models
from django.utils.text import slugify
from shared.models import Images, Gallery, Activity, Wildlife, Country, Month


class Destination(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="destinations"
    )
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to="destinations/image")
    description = models.TextField()

    homeof = models.CharField(max_length=100, blank=True, null=True)
    famousfor = models.CharField(max_length=100, blank=True, null=True)

    activities = models.ManyToManyField(Activity)
    wildlife = models.ManyToManyField(Wildlife)

    destination_map = models.ImageField(
        upload_to="destinations/map", blank=True, null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class DestinationLocation(models.Model):
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="location"
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class DestinationAnimalsOverview(models.Model):
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="animalsoverview"
    )
    mammal_species = models.CharField(max_length=50)
    identified_bird_species = models.CharField(max_length=50)
    amphibian_species = models.CharField(max_length=50)


class Highlights(models.Model):
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="highlights"
    )
    highlight_title = models.CharField(max_length=100)

    def __str__(self):
        return self.highlight_title

    class Meta:
        verbose_name_plural = "Highlights"


class DestinationMonth(models.Model):
    class MoodChoices(models.TextChoices):
        BEST = "BEST"
        GOOD = "GOOD"
        MIXED = "MIXED"

    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="months"
    )
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    when_to_visit = models.CharField(max_length=6, choices=MoodChoices.choices)

    def __str__(self) -> str:
        return f" {self.destination} - {self.month}"
