from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("aboutpage", views.aboutpage, name='aboutpage'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("login", views.login, name='login'),
    path("wallpapers", views.wallpapers, name='wallpapers'),
    path("log", views.blog, name='log'),
    path("wallpapers", views.wallpapers, name='wallpapers'),
    path("movies", views.movies, name='movies'),




   
]
