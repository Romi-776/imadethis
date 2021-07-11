from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
class IndexPage(ListView):
    model = Project
    template_name = "website/index.html"


class ProjectDetailsPage(DetailView):
    model = Project
    template_name = "website/project_details.html"
