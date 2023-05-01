from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from leads.models import Agent
from .forms import AgentModelForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        supervisor_team = self.request.user.supervisor
        return Agent.objects.filter(team=supervisor_team)


class AgentDetailView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        supervisor_team = self.request.user.supervisor
        return Agent.objects.filter(team=supervisor_team)


class AgentCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    success_url = reverse_lazy("agent-list")
    success_message = "New agent %(first_name)s %(last_name)s created successfully"

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.team = self.request.user.supervisor
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    success_url = reverse_lazy("agent-list")
    success_message = "Agent %(first_name)s %(last_name)s updated successfully"

    def get_queryset(self):
        supervisor_team = self.request.user.supervisor
        return Agent.objects.filter(team=supervisor_team)


class AgentDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    success_url = reverse_lazy("agent-list")
    success_message = "Agent deleted successfully"

    def get_queryset(self):
        supervisor_team = self.request.user.supervisor
        return Agent.objects.filter(team=supervisor_team)
