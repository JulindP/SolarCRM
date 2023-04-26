from django.urls import path

from .views import LeadList

urlpatterns = [
    path("", LeadList.as_view(), name="lead-list"),
]
