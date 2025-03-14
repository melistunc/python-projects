from django.urls import path
from . import views

#app_name register, url kısmına yazmak için. {% url 'app_name:index'%}
app_name = "template_app"

urlpatterns = [
    path("", views.index, name="index"), #boş bırakıldığında index'e gitsin.

    path("weather/", views.weather_view, name="weatherview"), #weather'e gidilince views.weather'e gidilsin.
] 