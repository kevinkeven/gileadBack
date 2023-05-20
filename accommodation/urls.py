from django.urls import path
from accommodation import views

urlpatterns = [
    # Accommodation URLs
    path("list/", views.AccommodationList.as_view()),
    path("create/", views.AccommodationCreate.as_view()),
    path("detail/<slug:slug>/", views.AccommodationDetail.as_view()),
    path("update/<slug:slug>/", views.AccommodationUpdate.as_view()),
    path("delete/<slug:slug>/", views.AccommodationDestroy.as_view()),
    path(
        "destination/<int:pk>/",
        views.AccommodationListByDestination.as_view(),
    ),
    # ExpertView URLs
    path("expert-views/", views.ExpertViewList.as_view()),
    path("expert-views/create/", views.ExpertViewCreate.as_view()),
    path("expert-views/<int:pk>/", views.ExpertViewDetail.as_view()),
    path("expert-views/<int:pk>/update/", views.ExpertViewUpdate.as_view()),
    path("expert-views/<int:pk>/delete/", views.ExpertViewDestroy.as_view()),
    path(
        "expert-views/accommodation/<int:pk>/",
        views.ExpertViewListByAccommodation.as_view(),
    ),
    # Glance URLs
    path("glances/", views.GlanceList.as_view()),
    path("glances/create/", views.GlanceCreate.as_view()),
    path("glances/<int:pk>/", views.GlanceDetail.as_view()),
    path("glances/<int:pk>/update/", views.GlanceUpdate.as_view()),
    path("glances/<int:pk>/delete/", views.GlanceDestroy.as_view()),
    path("glances/accommodation/<int:pk>/", views.GlanceListByAccommodation.as_view()),
    # InsiderTip URLs
    path("insider-tips/", views.InsiderTipList.as_view()),
    path("insider-tips/create/", views.InsiderTipCreate.as_view()),
    path("insider-tips/<int:pk>/", views.InsiderTipDetail.as_view()),
    path("insider-tips/<int:pk>/update/", views.InsiderTipUpdate.as_view()),
    path("insider-tips/<int:pk>/delete/", views.InsiderTipDestroy.as_view()),
    path(
        "insider-tips/accommodation/<int:pk>/",
        views.InsiderTipListByAccommodation.as_view(),
    ),
]
