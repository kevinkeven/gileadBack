from django.contrib import admin
from accommodation import models

# Register your models here.


class ExpertViewInline(admin.TabularInline):
    model = models.ExpertView
    extra = 1


class GlanceInline(admin.TabularInline):
    model = models.Glance
    extra = 1


class InsiderTipInline(admin.TabularInline):
    model = models.InsiderTip
    extra = 1


@admin.register(models.Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "destination",
        "image",
        "slug",
    )
    list_filter = ("name", "destination")
    search_fields = ("name", "destination")
    prepopulated_fields = {"slug": ("name",)}
    ordering = (
        "name",
        "destination",
    )
    inlines = [
        ExpertViewInline,
        GlanceInline,
        InsiderTipInline,
    ]
