import datetime
import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movielens.settings')
django.setup()

from movie_data.models import Movie, Critic, Review


csv_item = '/Users/Nic/TIY/W6/movielens/movielens/movie_data/data/u.item'
csv_data = '/Users/Nic/TIY/W6/movielens/movielens/movie_data/data/u.data'
csv_user = '/Users/Nic/TIY/W6/movielens/movielens/movie_data/data/u.user'

date_convert = '%d-%b-%Y'
date_convert1 = '%Y-%m-%d'

############### Handle Movie Data

def process_date(somedate):
    try:
        re_date = datetime.datetime.strptime(somedate, date_convert)
        re_date = datetime.datetime.strftime(re_date, date_convert1)
        return(re_date)
    except:
        print("NOPE")

def process_movie():
    i = 0
    with open(csv_item, encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['id',
                                               'title',
                                               'release'],
                                delimiter='|')

        for movie in reader:
            release = process_date(movie['release'])
            _, created = Movie.objects.get_or_create(id=movie['id'],
                                                     title=movie['title'],
                                                     release=release)
            print("MOVIE ", i)
            i += 1



############### Handle User data
def process_critic():
    i = 0

    with open(csv_user, encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['id', 'age', 'sex', 'occupation', 'zip'], delimiter='|')
        for user in reader:
            if type(user['zip']) != int:
                user['zip'] = 99999

            _, created = Critic.objects.get_or_create(id=user['id'],
                                                      age=user['age'],
                                                      sex=user['sex'],
                                                      zip_code=user['zip'])
            print("User ", i)
            i += 1


############### Handle review Data
def process_review():
    i = 0

    with open(csv_data, encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['user_id',
                                               'movie_id',
                                               'rating'],
                                delimiter='\t')

        for review in reader:
            try:
                critic = Critic.objects.get(id=review['user_id'])
                movie = Movie.objects.get(id=review['movie_id'])
                rating = review['rating']
                _, created = Review.objects.get_or_create(critic=critic, movie=movie, rating=rating)

                print("Review ", i)
                i += 1
            except:
                continue



process_movie()
process_critic()
process_review()
