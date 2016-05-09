import datetime
import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movielens.settings')
django.setup()

from movie_data.models import Movie, Critic, Review

csv_movie_data = '/Users/Nic/TIY/W6/movielens/movielens/movie_data/data/u.item'
csv_review_data = '/Users/Nic/TIY/W6/movielens/movielens/movie_data/data/u.data'
csv_user_data = '/Users/Nic/TIY/W6/movielens/movielens/movie_data/data/u.user'

date_convert = '%d-%b-%Y'
date_convert1 = '%Y-%m-%d'


############### Handle Movie Data

def process_date(somedate):
    try:
        re_date = datetime.datetime.strptime(somedate, date_convert)
        re_date = datetime.datetime.strftime(re_date, date_convert1)
        return (re_date)
    except:
        print("NOPE")


"""Data was already loaded. Adding to existing data"""


def add_to_movie():
    fieldnames = ['id', 'title', 'release', 'vhs_release', 'imdb']

    with open(csv_movie_data, encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter='|')

        for movie in reader:
            genre = movie[None]
            if Movie.objects.get(id = movie['id']):
                m = Movie.objects.get(id=movie['id'])
                m.imdb_link = movie['imdb']
                m.g_unknown = genre[0]
                m.g_action = genre[1]
                m.g_adventure = genre[2]
                m.g_animation = genre[3]
                m.g_children = genre[4]
                m.g_comedy = genre[5]
                m.g_crime = genre[6]
                m.g_documentary = genre[7]
                m.g_drama = genre[8]
                m.g_fantasy = genre[9]
                m.g_noir = genre[10]
                m.g_horror = genre[11]
                m.g_musical = genre[12]
                m.g_romance = genre[13]
                m.g_scifi = genre[14]
                m.g_thriller = genre[15]
                m.g_war = genre[16]
                m.g_western = genre[17]
                m.save()


def process_movie():
    i = 0
    with open(csv_movie_data, encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['id',
                                               'title',
                                               'release',
                                               'vhs_release',
                                               'imdb'],
                                delimiter='|')

        # load the data into movies
        for movie in reader:
            release = process_date(movie['release'])
            genre = movie[None]
            _, created = Movie.objects.get_or_create(id=movie['id'],
                                                     title=movie['title'],
                                                     release=release,
                                                     imdb_link=movie['imdb'],
                                                     g_unknown=genre[0],
                                                     g_action=genre[1],
                                                     g_adventure=genre[2],
                                                     g_animation=genre[3],
                                                     g_children=genre[4],
                                                     g_comedy=genre[5],
                                                     g_crime=genre[6],
                                                     g_documentary=genre[7],
                                                     g_drama=genre[8],
                                                     g_fantasy=genre[9],
                                                     g_noir=genre[10],
                                                     g_horror=genre[11],
                                                     g_musical=genre[12],
                                                     g_romance=genre[13],
                                                     g_scifi=genre[14],
                                                     g_thriller=genre[15],
                                                     g_war=genre[16],
                                                     g_western=genre[17],
                                                     )

            for movie in Movie.objects.values():
                movie['id']

            print("MOVIE ", movie)
            i += 1


############### Handle User data
def process_critic():
    i = 0

    with open(csv_user_data, encoding='latin_1') as f:
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

    with open(csv_review_data, encoding='latin_1') as f:
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


add_to_movie()
# process_critic()
# process_review()
