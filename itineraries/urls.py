from django.urls import path
from itineraries import views

urlpatterns = [
    # Itinerary URLs
    path("list/", views.ItineraryList.as_view()),
    path("create/", views.ItineraryCreate.as_view()),
    path("detail/<slug:slug>", views.ItineraryDetail.as_view()),
    path("update/<slug:slug>", views.ItineraryUpdate.as_view()),
    path("delete/<slug:slug>", views.ItineraryDelete.as_view()),
    # ItineraryActivity URLs
    path("activity/list/", views.ItineraryActivityList.as_view()),
    path("activity/create/", views.ItineraryActivityCreate.as_view()),
    path("activity/detail/<int:pk>", views.ItineraryActivityDetail.as_view()),
    path("activity/update/<int:pk>", views.ItineraryActivityUpdate.as_view()),
    path("activity/delete/<int:pk>", views.ItineraryActivityDelete.as_view()),
    # ItineraryMonth URLs
    path("month/list/", views.ItineraryMonthList.as_view()),
    path("month/create/", views.ItineraryMonthCreate.as_view()),
    path("month/detail/<int:pk>", views.ItineraryMonthDetail.as_view()),
    path("month/update/<int:pk>", views.ItineraryMonthUpdate.as_view()),
    path("month/delete/<int:pk>", views.ItineraryMonthDelete.as_view()),
    # DayByDay URLs
    path("daybyday/list/", views.dayByDayList.as_view()),
    path("daybyday/create/", views.dayByDayCreate.as_view()),
    path("daybyday/detail/<int:pk>", views.dayByDayDetail.as_view()),
    path("daybyday/update/<int:pk>", views.dayByDayUpdate.as_view()),
    path("daybyday/delete/<int:pk>", views.dayByDayDelete.as_view()),
    # Included URLs
    path("included/list/", views.IncludedList.as_view()),
    path("included/create/", views.IncludedCreate.as_view()),
    path("included/detail/<int:pk>", views.IncludedDetail.as_view()),
    path("included/update/<int:pk>", views.IncludedUpdate.as_view()),
    path("included/delete/<int:pk>", views.IncludedDelete.as_view()),
    # Excluded URLs
    path("excluded/list/", views.ExcludedList.as_view()),
    path("excluded/create/", views.ExcludedCreate.as_view()),
    path("excluded/detail/<int:pk>", views.ExcludedDetail.as_view()),
    path("excluded/update/<int:pk>", views.ExcludedUpdate.as_view()),
    path("excluded/delete/<int:pk>", views.ExcludedDelete.as_view()),
]
