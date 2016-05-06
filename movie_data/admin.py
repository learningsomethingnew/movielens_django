from django.contrib import admin

from .models import Movie, Critic, Review

admin.site.register(Movie)
admin.site.register(Critic)
admin.site.register(Review)
