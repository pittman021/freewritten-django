from freewritten.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bvl&k)h88gzpyez4w+#jb)$(qj3&(v@4e0)0xz4t-mg1lzqjf2'

DEBUG = True

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'freewritten_development',
        'USER': 'timpittman',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

ETHEREAL_USERNAME = 'addison68@ethereal.email' # using ethereal creds here for testing
ETHEREAL_PASSWORD = 'VxVZ4HcqTf3MgWeHnk' # using ethereal creds here for testing 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.ethereal.email'
EMAIL_HOST_USER = ETHEREAL_USERNAME
EMAIL_HOST_PASSWORD = ETHEREAL_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
