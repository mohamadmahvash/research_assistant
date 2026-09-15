from django.urls import path
from . import views

app_name = "inquiries"

urlpatterns = [
    path("", views.InquiriesRequestCreateView.as_view()),
    path("list/", views.InquiriesRequestListView.as_view()),
    path("<uuid:pk>/", views.InquiriesRequestDetailView.as_view()),
]
