# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b6c7dtxvl%9#50)gzfpuy(&#nhneq)4%=f-=#4ka$wywe%am04'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movielens',
        'USER': 'SomeOne',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}