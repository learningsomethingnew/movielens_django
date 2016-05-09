import datetime
from django.db import models
from django.utils import timesince
import datetime
from django.template import loader


# Things to do:
# Rename classes to singular
# movie_title to title
# drop movie_id and user_id in favor of built in id
# Reviews.user_id and movie_id remove _id

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release = models.DateField()
    avg_rating = models.FloatField(default=0.0)
    num_reviews = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

    def time_since_published(self):
        temp_date = datetime.datetime.strptime(self.release_date)

        return timesince.timesince(temp_date)



# 1|24|M|technician|85711
class Critic(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    zip_code = models.IntegerField()

    def __str__(self):
        return "{} Aged {}".format(self.sex, self.age)


# user id | item id | rating | timestamp.
# 253	465	5	891628467
class Review(models.Model):
    critic = models.ForeignKey(
        Critic,
        on_delete=models.CASCADE
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()



    def __str__(self):
        return "Movie - {}: Score - {}".format(self.movie,
                                               self.rating)

