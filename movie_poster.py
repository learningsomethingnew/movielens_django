import requests
import os
import django
import time

from BeautifulSoup import BeautifulSoup
import re


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movielens.settings')
django.setup()

from movie_data.models import Movie
from movielens.secrets import *


all_movies = Movie.objects.all()

for movie in all_movies:
    print(movie.imdb_link)



# CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
# KEY = API_KEY
#
# url = CONFIG_PATTERN.format(key=KEY)
# r = requests.get(url)
# config = r.json()