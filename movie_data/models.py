import datetime
from django.db import models
from django.utils import timesince
import datetime

# movie id | movie title | release date | video release date | IMDb URL | unknown | Action | Adventure |
# Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy | Film-Noir | Horror | Musical |
# Mystery | Romance | Sci-Fi | Thriller | War | Western |
#1|Toy Story (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)|0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0
class Movies(models.Model):
    movie_id = models.IntegerField( null = False )
    movie_title = models.CharField( max_length = 200 )
    release_date = models.DateField()

    def __str__(self):
        return self.movie_title

    def time_since_published(self):
        temp_date = datetime.datetime.strptime(self.release_date)
        return timesince.timesince(temp_date)



#1|24|M|technician|85711
class Users(models.Model):
    user_id = models.IntegerField()
    age = models.IntegerField()
    sex = models.CharField( max_length=1 )
    zip_code = models.IntegerField()

    def __str__(self):
        return self.user_id


# user id | item id | rating | timestamp.
#253	465	5	891628467
class Reviews(models.Model):
    user_id = models.ForeignKey(
        Users,
        on_delete=models.CASCADE
    )

    movie_id = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()
