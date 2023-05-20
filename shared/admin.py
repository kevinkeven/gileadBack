from django.contrib import admin
from shared.models import Gallery, Images, Wildlife, Activity, Country, Month, CountryMonth

# Register your models here.

admin.site.register(Gallery)
admin.site.register(CountryMonth)
admin.site.register(Month)


admin.site.register(Images)
admin.site.register(Wildlife)
admin.site.register(Activity)
admin.site.register(Country)
