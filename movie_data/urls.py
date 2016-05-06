from django.conf.urls import url

from . import views

app_name = 'movie_data'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Get movie id
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),

    # # move id results
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #
    # # GET /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]