from django.views import generic


class Homepage(generic.TemplateView):
    template_name = "base.html"


class LeadList(generic.ListView):
    pass
