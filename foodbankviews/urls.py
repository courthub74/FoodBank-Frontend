from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('michigan/', views.mich, name="mich"),
    path('detroit/', views.det, name="detroit"),
    path('farmington/', views.farm, name="farm"),
    path('farmhills/', views.farmhills, name="farmhills"),
    path('livonia/', views.livonia, name="livonia"),
    path('southfield/', views.southfield, name="southfield"),

    path('illinois/', views.illinois, name="illinois"),
    path('northchicago/', views.chicagonord, name="chicagonord"),
    path('westchicago/', views.westchi, name="westchi"),
    path('chicago/', views.chicago, name="chicago"),
    path('oakpark/', views.oakpark, name="oakpark"),
    path('peoria/', views.peoria, name="peoria"),

    path('northcarolina/', views.ncaro, name="northcarolina"),
    path('raleigh/', views.raleigh, name="raleigh"),
    path('willmington/', views.willmington, name="willmington"),
    path('hampstead/', views.hampstead, name="hampstead"),

    path('newyork/', views.newyork, name="newyork"),
    path('nyny/', views.manhattan, name="nyny"),
    path('brooklyn/', views.brooklyn, name="brooklyn"),
]
