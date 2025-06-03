import os

from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    default="oXPWQPA3C3sdBCuBeXUKq3LBp9YDJ33-306p9EAKf1ja1xkWnKY",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)
CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

# Email settings
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT", default="1025")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="alisinasultani@gmail.com")

# Site configuration
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven Clone Api"

# CORS settings
CORS_URLS_REGEX = os.getenv("CORS_URLS_REGEX", default="^api/.*$")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}


GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}
