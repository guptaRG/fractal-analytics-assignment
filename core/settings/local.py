from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += ['django_extensions']

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
