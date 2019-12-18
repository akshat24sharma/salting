from django.urls import path
from . import views  

urlpatterns = [
    path("",views.saltpost),
    path("second/",views.second),
    path("login/",views.login),
    
]