from django.urls import path
from . import views

urlpatterns = [
    path('', views.cerita_pengalaman_di_ATA, name ='cerita_pengalaman_di_ATA')
]