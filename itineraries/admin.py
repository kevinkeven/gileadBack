from django.contrib import admin
from itineraries.models import (
    itineraries,
    dayByDay,
    Included,
    Excluded,
    ItineraryActivity,
    ItineraryMonth,
)


class IncludedInline(admin.TabularInline):
    model = Included
    extra = 1


class ExcludedInline(admin.TabularInline):
    model = Excluded
    extra = 1


class ItineraryActivityInline(admin.TabularInline):
    model = ItineraryActivity
    extra = 1


class ItineraryMonthInline(admin.TabularInline):
    model = ItineraryMonth
    extra = 1


class dayByDayInline(admin.TabularInline):
    model = dayByDay
    extra = 1


@admin.register(itineraries)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "duration",
        "transport",
        "accommodation",
        "departureFrom",
        "price",
    )
    list_filter = ("name", "departureFrom")
    search_fields = ("name", "departureFrom")
    prepopulated_fields = {"slug": ("name",)}
    ordering = (
        "name",
        "departureFrom",
    )
    inlines = [
        IncludedInline,
        ExcludedInline,
        ItineraryActivityInline,
        ItineraryMonthInline,
        dayByDayInline,
    ]
