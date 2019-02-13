from django.shortcuts import render

# Create your views here.

def identitas_dirimu(request):
    return render(request, 'data_diri/identitas_dirimu.html', {})