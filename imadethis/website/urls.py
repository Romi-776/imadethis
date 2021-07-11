from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path("", IndexPage.as_view(), name="index_page"),
    path("project/<int:pk>", ProjectDetailsPage.as_view(), name="project_details_page"),
]
