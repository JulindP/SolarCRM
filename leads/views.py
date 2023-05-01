from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

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
    model = Lead
    context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    model = Lead
    context_object_name = "lead"


class LeadCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    success_url = reverse_lazy("lead-list")
    success_message = "New lead %(first_name)s %(last_name)s created successfully"


class LeadUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    model = Lead
    form_class = LeadModelForm
    success_url = reverse_lazy("lead-list")
    success_message = "Lead %(first_name)s %(last_name)s updated successfully"


class LeadDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    model = Lead
    success_url = reverse_lazy("lead-list")
    success_message = "Lead deleted successfully"
