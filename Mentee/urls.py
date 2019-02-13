from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_mentee, name ='list_mentee')
]