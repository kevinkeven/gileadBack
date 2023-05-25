from django.urls import path
from shared import views

urlpatterns = [
    # Image URLs
    path("images/", views.ImageList.as_view()),
    path("images/create/", views.ImageCreate.as_view()),
    path("images/<int:pk>/", views.ImageDetailDestroy.as_view()),
    path("images/<int:pk>/update/", views.ImageUpdate.as_view()),
    path("images/<int:pk>/delete/", views.ImageDetailDestroy.as_view()),
    # Country URLs
    path("country/", views.CountryList.as_view()),
    path("country/create/", views.CountryCreate.as_view()),
    path("country/dest/<int:pk>/", views.CountryDestinations.as_view()),
    path("country/<slug:slug>/", views.CountryDetail.as_view()),
    path("country/<slug:slug>/update/", views.CountryUpdate.as_view()),
    path("country/<slug:slug>/destinations/", views.CountryDestinationsList.as_view()),
    path("country/<slug:slug>/delete/", views.CountryDestroy.as_view()),
    # Activity URLs
    path("activities/", views.ActivityList.as_view()),
    path("activities/create/", views.ActivityCreate.as_view()),
    path("activities/<slug:slug>/", views.ActivityDetailDestroy.as_view()),
    path("activities/<slug:slug>/update/", views.ActivityUpdate.as_view()),
    path("activities/<slug:slug>/delete/", views.ActivityDetailDestroy.as_view()),
    path(
        "activities/<slug:slug>/destinations/", views.ActivityDestinationsList.as_view()
    ),
    # Wildlife URLs
    path("wildlife/", views.WildlifeList.as_view()),
    path("wildlife/create/", views.WildlifeCreate.as_view()),
    path("wildlife/<int:pk>/", views.WildlifeDetailDestroy.as_view()),
    path("wildlife/<int:pk>/update/", views.WildlifeUpdate.as_view()),
    path("wildlife/<int:pk>/delete/", views.WildlifeDetailDestroy.as_view()),
    # Gallery URLs
    path("gallery/", views.GalleryList.as_view()),
    path("gallery/create/", views.GalleryCreate.as_view()),
    path("gallery/<str:pk>/", views.GalleryDetail.as_view()),
    path("gallery/<str:pk>/update/", views.GalleryUpdate.as_view()),
    path("gallery/<str:pk>/delete/", views.GalleryDestroy.as_view()),
    path("gallery/<str:pk>/images/", views.GalleryImageList.as_view()),
]
