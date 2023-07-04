from django.db import models
from django.utils.text import slugify
from destination.models import Destination
from shared.models import Gallery, Activity, Wildlife


class Accommodation(models.Model):
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="accommodations"
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="accommodation_images/")
    luxury = models.BooleanField(default=False, blank=True, null=True)
    activities = models.ManyToManyField(
        Activity, limit_choices_to=models.Q(destination=models.F("destination"))
    )

    gallery = models.ForeignKey(
        Gallery,
        related_name="accommodation",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Glance(models.Model):
    accommodation = models.ForeignKey(
        Accommodation, on_delete=models.CASCADE, related_name="glance"
    )
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Glances"


class InsiderTip(models.Model):
    accommodation = models.ForeignKey(
        Accommodation, on_delete=models.CASCADE, related_name="insidertip"
    )
    description = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "InsiderTips"


class ExpertView(models.Model):
    accommodation = models.ForeignKey(
        Accommodation, on_delete=models.CASCADE, related_name="expertview"
    )
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ExpertViews"
