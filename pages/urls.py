from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name="anasayfa"),
    path('cv', views.cv, name="cv"),
    path('hakkimizda', views.hakkimizda, name="hakkimizda")
    
]         
