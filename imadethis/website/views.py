from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
class IndexPage(ListView):
    model = Project
    template_name = "website/index.html"
    ordering = ["-id"]

class ProjectDetailsPage(DetailView):
    model = Project
    template_name = "website/project_details.html"


class NewProjectPage(CreateView):
    model = Project
    template_name = "website/new_project.html"
    form_class = NewProjectForm


class NewCategoryPage(CreateView):
    model = Category
    template_name = "website/new_category.html"
    fields = "__all__"

class EditProjectDetailsPage(UpdateView):
    model = Project
    template_name = "website/edit_project_details.html"
    form_class = EditProjectForm


class DeleteProjectPage(DeleteView):
    model = Project
    template_name = "website/delete_project.html"
    success_url = reverse_lazy("index_page")
    
class CategoryPage(ListView):
    model = Category
    template_name = "website/specific_category.html"
    
    def get(self, request, cat):
        category_posts = Project.objects.filter(category=cat)
        return render(request, self.template_name, {
            "category": cat.capitalize(),
            "category_posts": category_posts,
        })