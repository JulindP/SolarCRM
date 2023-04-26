from django.contrib import admin
from django.urls import include, path

from leads.views import Homepage

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("admin/", admin.site.urls),
    path("leads/", include("leads.urls")),
]
