from django.contrib import admin
from accommodation import models

# Register your models here.

admin.site.register(models.ExpertView)
admin.site.register(models.Glance)
admin.site.register(models.InsiderTip)


@admin.register(models.Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
    list_filter = ("destination",)
    search_fields = ("name", "destination", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)
    filter_horizontal = ("activities",)
