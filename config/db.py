import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': "django.db.backends.sqlite3",
        'NAME': os.path.join(BASE_DIR, 'db3.sqlite'),

    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_new',
        'USER': 'postgres',
        'PASSWORD': 'cantripologo',
        'HOST': 'localhost',
        'PORT': '5432'

    }
}