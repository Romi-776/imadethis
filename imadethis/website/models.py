from django.db import models
from django.contrib.auth.models import User


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

    # todo
    # add other fields in this mode like photos, demo_videos

    def __str__(self):
        return f"{self.name} made by :- {self.made_by}"
