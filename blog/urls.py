from django.urls import path
from blog.views import (
    BlogList,
    BlogDetail,
    CategoryList,
    CategoryDetail,
    BlogCreate,
    BlogEdit,
)


urlpatterns = [
    path("list/", BlogList.as_view()),
    path("new/", BlogCreate.as_view()),
    path("detail/<slug:slug>/", BlogDetail.as_view()),
    path("edit/<int:id>/", BlogEdit.as_view()),
    path("category/", CategoryList.as_view()),
    path("category/<slug:slug>/", CategoryDetail.as_view()),
]
