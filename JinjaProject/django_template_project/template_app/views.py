from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return render(request, "template_app/first.html")

    #return render(request, "template_app/first.html") #render'in index.html'i açması gerekiyor. urls.py'a geldiğinde path'de boş bırakıldığında frist.html'i render'la diyoruz.

def weather_view(request):
    weather_dictioanry= {"Paris":"30", "Rome": "20", "Madrid":[5,8,20,25], "Bordeaux": {"morning":10, "evening":20},
    "user_premium": True,
    "test": "test test Test test"} #kullanıcı user_premium

    return render(request, "template_app/weather.html", context=weather_dictioanry) #context'teki veriyi kullanmak istersekk html dosyası içinde yazdığımız yazının yanına iki süslü parantez içinden burada belirttiğimiz key isimlerini gireriz.