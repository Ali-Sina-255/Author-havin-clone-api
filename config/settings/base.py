from datetime import timedelta
from pathlib import Path

import environ

env = environ.Env()

environ.Env.read_env()

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

BASE_DIR = ROOT_DIR / "apps"

ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1", "api"]


# DEBUG mode
DEBUG = env.bool("DEBUG", default=True)
# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


LOCAL_APPS = [
    "apps.users",
    "apps.common",
    "apps.profiles",
    "apps.articles",
    "apps.ratings",
]

THIRD_PARTY_APPS = [
    "drf_yasg",
    "rest_framework",
    "django_filters",
    "corsheaders",
    "djcelery_email",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "taggit",
]


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database settings
# Update these according to your setup, for now this is a placeholder
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ROOT_DIR
        / "db.sqlite3",  # Creates the SQLite database in the base directory
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Localization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

STATIC_ROOT = str(ROOT_DIR / "staticfile")

# Media files (uploads)
MEDIA_URL = "/media/"

MEDIA_ROOT = str(ROOT_DIR / "mediafile")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS settings (Optional)
CORS_URLS_REGEX = r"^api/.*$"

AUTH_USER_MODEL = "users.User"

ADMIN_URL = "supersecret/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
CELERY_TASK_SEND_SENT_EVENT = True

if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE

# for allauth account
SITE_ID = 1


# rest framework  settings

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_FILTER_BACKEND": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
}

REST_AUTH = {
    # Authentication settings
    "USE_JWT": True,  # Set to True if using JWT-based authentication (with dj-rest-auth.jwt_auth)
    "JWT_AUTH_COOKIE": "author-access-token",
    "JWT_AUTH_REFRESH_COOKIE": "author-refresh-token",
}

AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",  # Corrected typo: 'backend' instead of 'backend'
)
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "apps.user.serializers.CustomRegisterSerializer"
}

# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = "email"
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_METHODS = {"email"}  # Use email as the only login method

# Signup fields: 'email*', 'password1*', 'password2*' (required fields)
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

# This one remains valid
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),  # Corrected to be a tuple
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),  # Lifetime for access tokens
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),  # Corrected key name
    "ROTATE_REFRESH_TOKENS": True,  # Fixed typo in key
    "SIGNING_KEY": env("SIGNING_KEY"),  # Ensure this is set in your environment
    "USER_ID_FIELD": "id",  # Field that stores user ID
    "USER_ID_CLAIM": "user_id",  # Claim that holds user ID
}

ACCOUNT_SIGNUP_FIELDS = {
    "username": {
        "required": True,
    },
    "email": {
        "required": True,
    },
}
