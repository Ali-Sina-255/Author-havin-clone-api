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

# Email settings
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", default="mailhog")
EMAIL_PORT = os.getenv("EMAIL_PORT", default="1025")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", default="alisinasultani@gmail.com")

# Site configuration
DOMAIN = os.getenv("DOMAIN", default="localhost:8000")
SITE_NAME = os.getenv("SITE_NAME", default="Authors Haven Clone Api")

# CORS settings
CORS_URLS_REGEX = os.getenv("CORS_URLS_REGEX", default="^api/.*$")
CORS_URLS_REGEX = os.getenv("CORS_URLS_REGEX", default="^api/.*$")
