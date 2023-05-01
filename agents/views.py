from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from leads.models import Agent
from .forms import AgentModelForm
from .mixins import SupervisorAndLoginRequiredMixin


class AgentListView(SupervisorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        supervisor_team = self.request.user.supervisor
        return Agent.objects.filter(team=supervisor_team)


class AgentDetailView(SupervisorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        supervisor_team = self.request.user.supervisor
        return Agent.objects.filter(team=supervisor_team)


class AgentCreateView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.CreateView
):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    success_url = reverse_lazy("agent-list")
    success_message = "New agent %(first_name)s %(last_name)s created successfully"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_supervisor = False
        user.save()
        Agent.objects.create(user=user, team=self.request.user.supervisor)
        return super(AgentCreateView, self).form_valid(form)


class AgentUpdateView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.UpdateView
):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    success_url = reverse_lazy("agent-list")
    success_message = "Agent %(first_name)s %(last_name)s updated successfully"

    def get_queryset(self):
        supervisor_team = self.request.user.supervisor
        return Agent.objects.filter(team=supervisor_team)


class AgentDeleteView(
    SupervisorAndLoginRequiredMixin, SuccessMessageMixin, generic.DeleteView
):
    template_name = "agents/agent_delete.html"
    success_url = reverse_lazy("agent-list")
    success_message = "Agent deleted successfully"

    def get_queryset(self):
        supervisor_team = self.request.user.supervisor
        return Agent.objects.filter(team=supervisor_team)
