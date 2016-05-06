import datetime
import csv
# from movie_data.models import Movies

csv_file = '/Users/Nic/TIY/W6/movielens/movielens/movie_data/data/u.item'

date_convert = '%d-%b-%Y'
date_convert1 = '%Y-%m-%d'

def load_movies():
    with open(csv_file, encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title', 'release_date'], delimiter='|')

        for movie in reader:
           print(movie['movie_id'])

def process_date(somedate):
    try:
        re_date = datetime.datetime.strptime(somedate, date_convert)
        re_date = datetime.datetime.strftime(re_date, date_convert1)
        return(re_date)
    except:
        print("NOPE")


def process_name(movie_dict):
    pass


_, created = Teacher.objects.get_or_create(movie_id=movie['movie_id'], movie_title=movie['movie_title'], release_date=

load_movies()