from django.urls import path, include
from .views import  home

urlpatterns = [
    path('', home, name="home"),
    path('logins/', include('django.contrib.auth.urls'), name = "login"),

]