"""
URL configuration for gilead project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from gilead.sitemap import (
    destinationSitemap,
    blogSitemap,
    accommodationSitemap,
    CountrySitemap,
    itinerariesSitemap,
)
from django.conf.urls.static import static

sitemaps = {
    "destination": destinationSitemap,
    "blog": blogSitemap,
    "accommodation": accommodationSitemap,
    "country": CountrySitemap,
    "itinerary": itinerariesSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/accounts/", include("authemail.urls")),
    path("api/destination/", include("destination.urls")),
    path("api/accommodation/", include("accommodation.urls")),
    path("api/shared/", include("shared.urls")),
    path("api/enquire/", include("enquire.urls")),
    path("api/itineraries/", include("itineraries.urls")),
    path("api/blog/", include("blog.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # path("api/bookings/", include("bookings.urls")),
    # path("api/search/", include("search.urls")),
    # path("api/tours/", include("tours.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
