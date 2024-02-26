from . import views
from django.urls import path

app_name = "main"
urlpatterns = [
    path('', views.get_game, name="get_game")
]
