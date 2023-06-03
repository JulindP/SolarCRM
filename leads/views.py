from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from agents.forms import CustomUserCreationForm
from agents.mixins import SupervisorAndLoginRequiredMixin
from .forms import LeadModelForm, AssignAgentForm
from .models import Lead


class Homepage(generic.TemplateView):
    template_name = "base.html"


class SignupView(SuccessMessageMixin, generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    success_message = "New user %(first_name)s %(last_name)s created successfully"


# def leadlist(request):
#     leads = Lead.objects.all()
#     orders = Order.objects.all()
#     total_orders = orders.count()
#     luce_orders = orders.filter(product__order__name="Luce").count()
#     gas_orders = orders.filter(product__order__name="Gas").count()
#     luce_gas_orders = orders.filter(product__order__name="Luce & Gas").count()
#
#     context = {
#         "leads": leads,
#         "orders": orders,
#         "total_orders": total_orders,
#         "luce_orders": luce_orders,
#         "gas_orders": gas_orders,
#         "luce_gas_orders": luce_gas_orders,
#     }
#     return render(request, "leads/lead_list.html", context)

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        if self.request.user.is_supervisor:
            queryset = Lead.objects.filter(team=self.request.user.supervisor, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(team=self.request.user.agent.team, agent__isnull=False)
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        if self.request.user.is_supervisor:
            queryset = Lead.objects.filter(team=self.request.user.supervisor, agent__isnull=True)
            context.update({
                "unassigned_leads": queryset
            })
        return context


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        if self.request.user.is_supervisor:
            queryset = Lead.objects.filter(team=self.request.user.supervisor)
        else:
            queryset = Lead.objects.filter(team=self.request.user.agent.team)
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset


class LeadCreateView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.CreateView
):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    success_url = reverse_lazy("lead-list")
    success_message = "New lead %(first_name)s %(last_name)s created successfully"


class LeadUpdateView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.UpdateView
):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    success_url = reverse_lazy("lead-list")
    success_message = "Lead %(first_name)s %(last_name)s updated successfully"

    def get_queryset(self):
        return Lead.objects.filter(team=self.request.user.supervisor)


class LeadDeleteView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.DeleteView
):
    template_name = "leads/lead_delete.html"
    success_url = reverse_lazy("lead-list")
    success_message = "Lead deleted successfully"

    def get_queryset(self):
        return Lead.objects.filter(team=self.request.user.supervisor)


class AssignAgentView(SupervisorAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm
    success_url = reverse_lazy("lead-list")

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs()
        kwargs.update({
            "request": self.request
        })
        return kwargs
    
    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)