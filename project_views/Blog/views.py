from django.shortcuts import render

# Create your views here.

def cerita_pengalaman_di_ATA(request):
    return render(request, 'latar/cerita_pengalaman_di_ATA.html', {})