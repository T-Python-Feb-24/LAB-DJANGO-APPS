from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_page(reguest:HttpRequest):
    return render(reguest,"main/game.html")