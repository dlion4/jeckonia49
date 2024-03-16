import os
from .common import *
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True


# Mail
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



CORS_ALLOWED_ORIGINS = [] # add the frotned domain that will consume the api endppint


CSRF_TRUSTED_ORIGINS = [
    "http://localhost", "https://*.ngrok-free.app"
] # needed for post request
