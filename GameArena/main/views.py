from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def Game_View(request:HttpRequest):
    return render(request,"games/index.html")