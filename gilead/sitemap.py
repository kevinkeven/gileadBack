from typing import Union
from django.contrib.sitemaps import (
    Sitemap,
)
from django.db.models.base import Model
from destination.models import Destination
from itineraries.models import itineraries
from accommodation.models import Accommodation
from shared.models import Country
from blog.models import Post


class destinationSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = "https"

    def items(self):
        return Destination.objects.all()

    def location(self, obj):
        return f"/destination/{obj.slug}"


class blogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = "https"

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return f"/blog/{obj.slug}"


class itinerariesSitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = "https"

    def items(self):
        return itineraries.objects.all()

    def location(self, obj):
        return f"/itineraries/detail/{obj.slug}"


class accommodationSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Accommodation.objects.all()

    def location(self, obj):
        return f"/accommodation/{obj.slug}"


class CountrySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = "https"

    def items(self):
        return Country.objects.all()

    def location(self, obj):
        return f"Country/{obj.slug}"
