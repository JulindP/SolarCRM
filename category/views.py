from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from leads.models import Lead
from .models import Category


# Create your views here.
class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "categories/category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)

        if self.request.user.is_supervisor:
            queryset = Lead.objects.filter(team=self.request.user.supervisor)
        else:
            queryset = Lead.objects.filter(team=self.request.user.agent.team)

        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count(),
            "contacted_lead_count": queryset.filter(category__name="Contacted").count(),
            "converted_lead_count": queryset.filter(category__name="Converted").count(),
            "unconverted_lead_count": queryset.filter(category__name="Unconverted").count(),
        })
        return context

    def get_queryset(self):
        if self.request.user.is_supervisor:
            queryset = Category.objects.filter(team=self.request.user.supervisor)
        else:
            queryset = Category.objects.filter(team=self.request.user.agent.team)
        return queryset


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "categories/category_detail.html"
    context_object_name = "category"

    def get_queryset(self):
        if self.request.user.is_supervisor:
            queryset = Category.objects.filter(team=self.request.user.supervisor)
        else:
            queryset = Category.objects.filter(team=self.request.user.agent.team)
        return queryset

