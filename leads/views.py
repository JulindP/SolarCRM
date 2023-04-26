from django.views import generic
from .models import Lead


class Homepage(generic.TemplateView):
    template_name = "base.html"


class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    model = Lead
