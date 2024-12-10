from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 24401235))
    API_HASH = env.get("TELEGRAM_API_HASH", "149f7e13d7d861b27cffc3ab1fd52b22")
    OWNER_ID = int(env.get("OWNER_ID", 1556830659))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "5546204735 655594746 1556830659 764052306").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Hdt_stree_2_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7705751598:AAFyX6YrCCWTZQ2hSFHd2hCHYsnSjWKvQ90")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002464478619))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 24))

class Server:
    BASE_URL = env.get("BASE_URL", "http://185.170.112.86:7777")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 7777))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
