from .common import *

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')

# DJANGO_LOG_LEVEL = env('DJANGO_LOG_LEVEL')