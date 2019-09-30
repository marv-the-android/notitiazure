from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainMap(request):
    return render(request, 'mainmap.html')
