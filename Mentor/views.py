from django.shortcuts import render

# Create your views here.

def kegiatan_kegiatan_ATA(request):
    return render(request, 'pengajar/list_mentor.html', {})