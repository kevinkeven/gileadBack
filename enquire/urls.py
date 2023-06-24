from django.urls import path
from enquire import views


urlpatterns = [
    path("", views.EnquireList.as_view()),
    path("create/", views.EnquireCreate.as_view()),
    path("delete/<uuid:pk>/", views.EnquirerDelete.as_view()),
    # path(""),
    path("contact-us/list", views.ContactUsList.as_view()),
    path("contact-us/create", views.ContactUsCreate.as_view()),
    path("contact-us/detail", views.ContactUsRetrieveDelete().as_view()),
]
