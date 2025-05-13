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
        'file_solid': {
            'class': 'logging.FileHandler',
            'filename': 'file_solid.log',
            'mode': 'a',
            'level': 'DEBUG',
            'formatter': 'detailed',
        },
        'file_pattern_factory': {
            'class': 'logging.FileHandler',
            'filename': 'file_pattern_factory.log',
            'mode': 'a',
            'level': 'DEBUG',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'solid': {
            'handlers': ['console', 'file_solid'],
            'level': 'DEBUG',
            'propagate': False
        },
        'pattern_factory': {
            'handlers': ['console', 'file_pattern_factory'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}