from gardens.settings.common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['glacial-reaches-33941.herokuapp.com']

# SENGRID_USERNAME = os.getenv('SENDGRID_USERNAME')
# SENDGRID_PASSWORD = os.getenv('SENDGRID_PASSWORD')

# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = SENGRID_USERNAME
# EMAIL_HOST_PASSWORD = SENDGRID_PASSWORD
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True