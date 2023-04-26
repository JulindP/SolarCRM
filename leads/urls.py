from django.urls import path

from .views import LeadListView

urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
]
