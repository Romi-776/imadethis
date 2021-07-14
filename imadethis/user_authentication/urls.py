from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path("register/", RegistrationPage.as_view(), name="registration_page"),
]
