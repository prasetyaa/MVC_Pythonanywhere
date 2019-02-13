from django.shortcuts import render

# Create your views here.

def list_mentee(request):
    return render(request, 'peserta/list_mentee.html', {})