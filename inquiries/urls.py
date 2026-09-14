from django.urls import path
from . import api_views

app_name = "inquiries"

urlpatterns = [
    path("", api_views.InquiriesRequestCreateAPIView.as_view()),
    path("list/", api_views.InquiriesRequestListAPIView.as_view()),
    path("<uuid:pk>/", api_views.InquiriesRequestDetailAPIView.as_view()),
]
