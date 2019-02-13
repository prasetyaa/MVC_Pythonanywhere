from django.urls import path
from . import views

urlpatterns = [
    path('', views.kegiatan_kegiatan_ATA, name ='kegiatan_kegiatan_ATA')
]