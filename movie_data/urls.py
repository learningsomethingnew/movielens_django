from django.conf.urls import url

from .views import detail, index, critic, top

app_name = 'movie_data'

urlpatterns = [
    url(r'^$', index, name='index'),

    # Get movie id
    url(r'^movie/(?P<movie_id>[0-9]+)/$', detail, name='detail'),

    # move id results
    url(r'^critic/(?P<critic_id>[0-9]+)/$', critic, name='critic'),

    # top 20 movies
    url(r'^top(?P<num>[0-9]+)/$', top, name='top'),

    # Login information
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout'),

    # # GET /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]