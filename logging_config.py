LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'app_pattern_factory.log',
            'mode': 'a',
            'level': 'DEBUG',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'solid': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}