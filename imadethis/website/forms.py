from django import forms
from .models import *

categories = Category.objects.all().values_list('name', 'name')

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Project Name"}),
            "made_by": forms.Select(attrs={"class": "form-control", "placeholder": "Who made it?"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Project Description"}),
            "category": forms.Select(choices=categories, attrs={"class": "form-control", "placeholder": "Project Category"}),
            "link": forms.TextInput(attrs={"class": "form-control", "placeholder": "URL to the Project"}),
        }
        
class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "category", "link"]
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Project Name"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Project Description"}),
            "category": forms.Select(choices=categories, attrs={"class": "form-control", "placeholder": "Project Category"}),
            "link": forms.TextInput(attrs={"class": "form-control", "placeholder": "URL to the Project"}),
        }