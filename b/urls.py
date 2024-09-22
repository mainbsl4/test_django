from django.urls import path
from .views import BList, BDetail

urlpatterns = [
    path("b/list/", BList.as_view(), name="b-list"),
    path("b/detail/<int:pk>/", BDetail.as_view(), name="b-detail"),
]
