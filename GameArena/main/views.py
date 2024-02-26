from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
def home(request):
    return render(request, 'main/home.html')
