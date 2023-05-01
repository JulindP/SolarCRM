from django import forms
from .models import Lead


class LeadCreateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "agent": forms.Select(attrs={"class": "form-control"}),
        }
