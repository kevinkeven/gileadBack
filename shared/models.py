from django.db import models
from django.utils.text import slugify


class Images(models.Model):
    image = models.ImageField(upload_to="gallery_images/")
    caption = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        image_url = self.image.name
        split_image_url = image_url.split("/")
        image_name = split_image_url[-1]
        return image_name

    class Meta:
        verbose_name_plural = "Images"


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField(Images, related_name="gallery")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Galleries"


class Wildlife(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Wildlifes"


class Activity(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Activities"


class Country(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)
    slogan = models.CharField(max_length=150)
    title = models.CharField(max_length=50)
    famousfor = models.CharField(max_length=80)
    peaktime = models.CharField(max_length=80)
    homeof = models.CharField(max_length=80)
    image = models.ImageField(upload_to="country/images")
    description = models.TextField()
    gallery = models.ForeignKey(
        "Gallery", related_name="country", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Countries"
class Month(models.Model):
    name = models.CharField(max_length=20, primary_key=True ,unique=True)

    def __str__(self) -> str:
        return self.name
    
class CountryMonth(models.Model):

    class MoodChoices(models.TextChoices):
        BEST = "BEST"
        GOOD = "GOOD"
        MIXED = "MIXED"
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="months")
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    when_to_visit = models.CharField(max_length=6, choices=MoodChoices.choices)

    def __str__(self) -> str:
        return f'Month for {self.destination}'
