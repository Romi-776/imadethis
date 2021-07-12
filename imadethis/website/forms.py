from django import forms
from .models import *


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Project Name"}),
            "made_by": forms.Select(attrs={"class": "form-control", "placeholder": "Who made it?"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Project Description"}),
            "link": forms.TextInput(attrs={"class": "form-control", "placeholder": "URL to the Project"}),
        }