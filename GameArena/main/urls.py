from . import views
from django.urls import path,include

app_name = "main"

urlpatterns = [
    path("game/dlc" ,views.Game_View , name="Game view"),
]