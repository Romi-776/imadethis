from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
class IndexPage(ListView):
    model = Project
    template_name = "website/index.html"


class ProjectDetailsPage(DetailView):
    model = Project
    template_name = "website/project_details.html"


class NewProjectPage(CreateView):
    model = Project
    template_name = "website/new_project.html"
    form_class = NewProjectForm


class EditProjectDetailsPage(UpdateView):
    model = Project
    template_name = "website/edit_project_details.html"
    form_class = EditProjectForm


class DeleteProjectPage(DeleteView):
    model = Project
    template_name = "website/delete_project.html"
    success_url = reverse_lazy("index_page")