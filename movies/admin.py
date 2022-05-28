from turtle import title
from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "release_year", "genre")
    exclude = ("date_created",)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
