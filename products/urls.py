from django.urls import path

from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<int:pk>", ProductDetailView.as_view(), name="product-detail"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="product-update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product-delete"),
]
