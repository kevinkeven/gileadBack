from django.contrib import admin
from shared.models import (
    Gallery,
    Images,
    Wildlife,
    Activity,
    Country,
    Month,
    CountryMonth,
    countryFamous,
    countryHomeOf,
)

# Register your models here.

admin.site.register(Gallery)
admin.site.register(CountryMonth)
admin.site.register(Month)


admin.site.register(Images)
admin.site.register(Wildlife)
admin.site.register(Activity)


class CountryMonthInline(admin.TabularInline):
    model = CountryMonth
    extra = 1


class countryFamousInline(admin.TabularInline):
    model = countryFamous
    extra = 1


class countryHomeOfInline(admin.TabularInline):
    model = countryHomeOf
    extra = 1


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [CountryMonthInline, countryFamousInline, countryHomeOfInline]
    prepopulated_fields = {"slug": ("name",)}
