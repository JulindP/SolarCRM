from django.urls import path

from .views import (
    LeadListView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView,
)

urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
    path("<int:pk>", LeadDetailView.as_view(), name="lead-detail"),
    path("create/", LeadCreateView.as_view(), name="lead-create"),
    path("update/<int:pk>/", LeadUpdateView.as_view(), name="lead-update"),
    path("delete/<int:pk>", LeadDeleteView.as_view(), name="lead-delete"),
]
