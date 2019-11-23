# -*- coding: utf-8 -*-
"""log settings"""

import os

LOG_DIR = os.environ.get('LOG_DIR', '.')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
    },
    'handlers': {
        'console': {
            'level': os.environ.get('CONSOLE_LOG_LEVEL', 'INFO'),
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'verbose'
        },
        "sql": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],
            "formatter": "verbose",
        },
        'file': {
            'level': os.environ.get('FILE_LOG_LEVEL', 'INFO'),
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'backupCount': 10,
            'filename': os.path.join(LOG_DIR, 'platform.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'core': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'INFO',
            'handlers': ['sql'],
            'propagate': False,
        },
    }
}
