from django.contrib import admin
from destination import models

# Register your models here.
admin.site.register(models.TravelTip)
admin.site.register(models.DestinationMonth)
admin.site.register(models.DestinationAnimalsOverview)
admin.site.register(models.DestinationLocation)
admin.site.register(models.DestinationTransport)





# admin.site.register(models.Months)
admin.site.register(models.Highlights)


@admin.register(models.Destination)
class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
