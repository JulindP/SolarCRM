from django.urls import path

from .views import (
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
)

urlpatterns = [
    path("", OrderListView.as_view(), name="order-list"),
    path("<int:pk>", OrderDetailView.as_view(), name="order-detail"),
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("update/<int:pk>/", OrderUpdateView.as_view(), name="order-update"),
    path("delete/<int:pk>", OrderDeleteView.as_view(), name="order-delete"),
]
