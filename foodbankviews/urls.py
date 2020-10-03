from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('michigan/', views.mich, name="mich"),
    path('farmington/', views.farm, name="farm"),
]
