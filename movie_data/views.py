from django.http import HttpResponse
from .models import Movie, Critic, Review
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'movies/index.html', {'all_movies': Movie.objects.all()})


def detail(request, movie_id):
    all_movies = get_object_or_404(Movie, id=movie_id)
    movies_reviewed = Review.objects.filter(movie=movie_id)
    return render(request, 'movies/detail.html', {'movie': all_movies, 'reviewed': movies_reviewed})


def critic(request, critic_id):
    all_critics = get_object_or_404(Critic, id=critic_id)
    movies_reviewed = Review.objects.filter(critic=critic_id)
    return render(request, 'movies/critic.html',
                  {'critic': all_critics,
                   'reviewed': movies_reviewed}
                  )


def top(request, num=20):
    top_n = Movie.get_top(num)
    return render(request,
                  'movies/top.html',
                  {'top': top_n}
                  )


# Search Functionality
def search_form(request):
    return render(request, 'movies/search_form.html', {'error': False})


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            movie_search = Movie.objects.filter(title__icontains=q)
            return render(request, 'movies/search.html',
                          {'movie_search': movie_search,
                           'query': q
                           })
    return render(request, 'movies/search_form.html', {'error': error})

