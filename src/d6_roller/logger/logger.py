import logging
import logging.config

LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s | %(levelname)s | %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
}

logging.config.dictConfig(LOG_CONFIG)

logger = logging.getLogger()
