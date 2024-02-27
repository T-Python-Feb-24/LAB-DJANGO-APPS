from django.shortcuts import render
from djang.http import HttpRequest,HttpResponse

# Create your views here.
def home_page(request:HttpRequest):
    return render(request,'main/index.html')