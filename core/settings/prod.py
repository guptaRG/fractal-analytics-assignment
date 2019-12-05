# -*- coding: utf-8 -*-
"""
Settings for running the application in production
"""
from .common import *

DEBUG = False

ALLOWED_HOSTS += ['django']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

CORS_ORIGIN_WHITELIST = ["localhost:3000", "127.0.0.1:3000", "0.0.0.0:3000"]
