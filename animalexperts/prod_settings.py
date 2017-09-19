'''
Production settings file
'''

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'animalexperts',
        'USER': 'django',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': ''
    }
}

INSTALLED_APPS += ['django.contrib.postgres']
