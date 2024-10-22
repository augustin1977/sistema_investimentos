from django.urls import path
from . import views
# cria os caminhos para acesso as views
from django.urls import path
from . import views
# cria os caminhos para acesso as views
urlpatterns = [
    path("",views.home, name="home"),
    
    
]