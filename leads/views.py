from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic

from agents.mixins import SupervisorAndLoginRequiredMixin
from .forms import CustomUserCreationForm, LeadModelForm
from .models import Lead


class SignupView(SuccessMessageMixin, generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    success_message = "New user %(first_name)s %(last_name)s created successfully"


class Homepage(generic.TemplateView):
    template_name = "base.html"


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        if self.request.user.is_supervisor:
            queryset = Lead.objects.filter(team=self.request.user.supervisor)
        else:
            queryset = Lead.objects.filter(team=self.request.user.agent.team)
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset


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

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"],
        )
        return super(LeadCreateView).form_valid(form)


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
