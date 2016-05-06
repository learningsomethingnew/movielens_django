from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the movie_data index.")


def detail(request, movie_id):
    return HttpResponse("You're looking at move %s." % movie_id)
