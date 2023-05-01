from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from leads.models import Agent
from .forms import AgentModelForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    model = Agent
    context_object_name = "agents"


class AgentCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    success_url = reverse_lazy("agent-list")
    success_message = "New agent %(first_name)s %(last_name)s created successfully"
