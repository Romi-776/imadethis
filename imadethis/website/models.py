from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("index_page")


class Project(models.Model):
    """
        Project model to store data related to Projects.
    """

    name = models.CharField(max_length=256)
    made_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="project_owner"
    )
    description = models.TextField()
    link = models.URLField(max_length=256)
    published_at = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="Other")
    # todo
    # add other fields in this mode like photos, demo_videos

    def __str__(self):
        return f"{self.name} made by :- {self.made_by}"

    def get_absolute_url(self):
        return reverse("project_details_page", args=str(self.pk))

