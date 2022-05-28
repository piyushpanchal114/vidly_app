from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, "movies/index.html", {"movies": movies})


def detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    #movie = Movie.objects.get(pk=pk)
    return render(request, "movies/detail.html", {"movie": movie})


def home(request):
    return render(request, "movies/home.html")
