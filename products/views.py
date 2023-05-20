from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic

from agents.mixins import SupervisorAndLoginRequiredMixin
from .forms import ProductModelForm
from .models import Product


class ProductListView(LoginRequiredMixin, generic.ListView):
    template_name = "products/product_list.html"
    model = Product
    context_object_name = "products"

    # def get_queryset(self):
    #     if self.request.user.is_supervisor:
    #         queryset = Sale.objects.filter(team=self.request.user.supervisor)
    #     else:
    #         queryset = Sale.objects.filter(team=self.request.user.agent.team)
    #         queryset = queryset.filter(agent__user=self.request.user)
    #     return queryset


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "products/product_detail.html"
    model = Product
    context_object_name = "product"

    # def get_queryset(self):
    #     if self.request.user.is_supervisor:
    #         queryset = Order.objects.filter(team=self.request.user.supervisor)
    #     else:
    #         queryset = Sale.objects.filter(team=self.request.user.agent.team)
    #         queryset = queryset.filter(agent__user=self.request.user)
    #     return queryset


class ProductCreateView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.CreateView
):
    template_name = "products/product_create.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")
    success_message = "New product is created successfully."

    def form_valid(self, form):
        send_mail(
            subject="A sale has been created",
            message="Go to the site to see the new sale",
            from_email="test@test.com",
            recipient_list=["test2@test.com"],
        )
        return super(ProductCreateView).form_valid(form)


class ProductUpdateView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.UpdateView
):
    template_name = "products/product_update.html"
    form_class = ProductModelForm
    model = Product
    success_url = reverse_lazy("order-list")
    success_message = "Product updated successfully"

    # def get_queryset(self):
    #     return Order.objects.filter(team=self.request.user.supervisor)


class ProductDeleteView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.DeleteView
):
    template_name = "products/product_detail.html"
    model = Product
    success_url = reverse_lazy("order-list")
    success_message = "Product deleted successfully"

    # def get_queryset(self):
    #     return Order.objects.filter(team=self.request.user.supervisor)

