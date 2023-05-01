from django.urls import path

from .views import (
    AgentCreateView,
    AgentDeleteView,
    AgentDetailView,
    AgentListView,
    AgentUpdateView,
)

urlpatterns = [
    path("", AgentListView.as_view(), name="agent-list"),
    path("<int:pk>", AgentDetailView.as_view(), name="agent-detail"),
    path("create/", AgentCreateView.as_view(), name="agent-create"),
    path("update/<int:pk>/", AgentUpdateView.as_view(), name="agent-update"),
    path("delete/<int:pk>", AgentDeleteView.as_view(), name="agent-delete"),
]
