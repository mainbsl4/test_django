from django.urls import path
from .views import AList, ADetail


urlpatterns = [
    path("a/list/", AList.as_view(), name="a-list"),
    path("a/detail/<int:pk>/", ADetail.as_view(), name="a-detail"),
]
