from django.urls import path
from . import views

urlpatterns = [
    path("movies/", views.index, name="index"),
    path("movies/<int:id>", views.detail, name="movie_detail"),
    path("", views.home, name="home")
]
