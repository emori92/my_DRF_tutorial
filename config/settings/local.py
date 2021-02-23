from .base import *


# secure
DEBUG = True
SECRET_KEY = 'VUE-CDN-SAMPLE-APP-SECRET-KEY'

# db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}