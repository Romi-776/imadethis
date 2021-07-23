from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path("", IndexPage.as_view(), name="index_page"),
    path("project/<int:pk>", ProjectDetailsPage.as_view(), name="project_details_page"),
    path("new_project/", NewProjectPage.as_view(), name="new_project_page"),
    path("project/edit/<int:pk>", EditProjectDetailsPage.as_view(), name="edit_project_details_page"),
    path("project/delete/<int:pk>", DeleteProjectPage.as_view(), name="delete_project_page"),
    path('new_category/', NewCategoryPage.as_view(), name="new_category_page"),
    path("category/<str:cat>/", CategoryPage.as_view(), name="specific_category_page"),
]
