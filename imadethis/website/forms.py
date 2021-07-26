from django import forms
from .models import *


categories = Category.objects.all().values_list("name", "name")


class DateInput(forms.DateInput):
    input_type = "date"


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "made_by",
            "description",
            "category",
            "created_why",
            "for_whom",
            "start_date",
            "end_date",
            "link",
        )

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Project Name"}
            ),
            "made_by": forms.Select(
                attrs={"class": "form-control", "placeholder": "Who made it?"}
            ),
            "category": forms.Select(
                choices=categories,
                attrs={"class": "form-control", "placeholder": "Category of Project"},
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Project Description"}
            ),
            "created_why": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Why you created this project?",
                }
            ),
            "for_whom": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Why you created this project?",
                }
            ),
            "start_date": DateInput(),
            "end_date": DateInput(),
            "link": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "URL to the Project"}
            ),
        }

    def clean(self):
        self.cleaned_data['category'] = self.cleaned_data['category'].lower()


class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "link", "category"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Project Name"}
            ),
            "category": forms.Select(
                choices=categories,
                attrs={"class": "form-control", "placeholder": "Category of Project"},
            ),
            "link": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "URL to the Project"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Project Description"}
            ),
        }
