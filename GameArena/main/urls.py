from.import views
from Django.urls import path

App_name ='main'

Urlpatterns =[
    path('',views.home_page,name="home_page")
]