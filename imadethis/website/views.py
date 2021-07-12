from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import NewProjectForm
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
