from django.contrib import admin
from destination import models


class HighlightInline(admin.TabularInline):
    model = models.Highlights
    extra = 1


class DestinationLocationInline(admin.TabularInline):
    model = models.DestinationLocation
    extra = 1


class DestinationAnimalsOverviewInline(admin.TabularInline):
    model = models.DestinationAnimalsOverview
    extra = 1


class DestinationMonthInline(admin.TabularInline):
    model = models.DestinationMonth
    extra = 1


@admin.register(models.Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "description",
        "image",
        "slug",
    )
    list_filter = ("name", "country")
    search_fields = ("name", "country")
    prepopulated_fields = {"slug": ("name",)}
    ordering = (
        "name",
        "country",
    )
    inlines = [
        HighlightInline,
        DestinationLocationInline,
        DestinationAnimalsOverviewInline,
        DestinationMonthInline,
    ]
