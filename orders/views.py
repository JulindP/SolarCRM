from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic

from agents.mixins import SupervisorAndLoginRequiredMixin
from orders.forms import OrderModelForm
from orders.models import Order


class OrderListView(LoginRequiredMixin, generic.ListView):
    template_name = "orders/order_list.html"
    model = Order
    context_object_name = "orders"

    # def get_queryset(self):
    #     if self.request.user.is_supervisor:
    #         queryset = Sale.objects.filter(team=self.request.user.supervisor)
    #     else:
    #         queryset = Sale.objects.filter(team=self.request.user.agent.team)
    #         queryset = queryset.filter(agent__user=self.request.user)
    #     return queryset


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "orders/order_detail.html"
    model = Order
    context_object_name = "order"

    # def get_queryset(self):
    #     if self.request.user.is_supervisor:
    #         queryset = Order.objects.filter(team=self.request.user.supervisor)
    #     else:
    #         queryset = Sale.objects.filter(team=self.request.user.agent.team)
    #         queryset = queryset.filter(agent__user=self.request.user)
    #     return queryset


class OrderCreateView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.CreateView
):
    template_name = "orders/order_create.html"
    form_class = OrderModelForm
    success_url = reverse_lazy("order-list")
    success_message = "New sale is created successfully."

    def form_valid(self, form):
        send_mail(
            subject="A sale has been created",
            message="Go to the site to see the new sale",
            from_email="test@test.com",
            recipient_list=["test2@test.com"],
        )
        return super(OrderCreateView).form_valid(form)


class OrderUpdateView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.UpdateView
):
    template_name = "orders/order_update.html"
    form_class = OrderModelForm
    model = Order
    success_url = reverse_lazy("order-list")
    success_message = "Sale updated successfully"

    # def get_queryset(self):
    #     return Order.objects.filter(team=self.request.user.supervisor)


class OrderDeleteView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.DeleteView
):
    template_name = "orders/order_detail.html"
    model = Order
    success_url = reverse_lazy("order-list")
    success_message = "Sale deleted successfully"

    # def get_queryset(self):
    #     return Order.objects.filter(team=self.request.user.supervisor)
