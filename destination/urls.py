from django.urls import path
from destination import views

urlpatterns = [
    # Destination URLs
    path("list/", views.DestinationList.as_view()),
    path("create/", views.DestinationCreate.as_view()),
    path("detail/<slug:slug>", views.DestinationDetail.as_view()),
    path("update/<slug:slug>", views.DestinationUpdate.as_view()),
    path("delete/<slug:slug>", views.DestinationDestroy.as_view()),
    # TravelTip URLs
    path("travel-tips/", views.TravelTipList.as_view()),
    path("travel-tips/create", views.TravelTipCreate.as_view()),
    path("travel-tips/<int:pk>", views.TravelTipDetail.as_view()),
    path("travel-tips/<int:pk>/update", views.TravelTipUpdate.as_view()),
    path("travel-tips/<int:pk>/delete", views.TravelTipDestroy.as_view()),
    # Highlights URLs
    path("highlights/", views.HighlightsList.as_view()),
    path("highlights/create/", views.HighlightsCreate.as_view()),
    path("highlights/<int:pk>", views.HighlightsDetail.as_view()),
    path("highlights/<int:pk>/update", views.HighlightsUpdate.as_view()),
    path("highlights/<int:pk>/delete", views.HighlightsDestroy.as_view()),
    path(
        "highlights/destination/<int:pk>",
        views.HighlightsListByDestination.as_view(),
    ),
    #DestinationActivities
    # path("activities/<int:pk>/", views.DestinationActivitiesList.as_view()),

]
