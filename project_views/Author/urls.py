from django.urls import path
from . import views

urlpatterns = [
    path('', views.identitas_dirimu, name ='identitas_dirimu')
]