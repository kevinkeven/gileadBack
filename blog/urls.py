from django.urls import path
from blog.views import BlogList, BlogDetail, CategoryList, CategoryDetail


urlpatterns = [
    path("list/", BlogList.as_view()),
    path("detail/<slug:slug>/", BlogDetail.as_view()),
    path("category/", CategoryList.as_view()),
    path("category/<slug:slug>/", CategoryDetail.as_view()),
]
