from datetime import timedelta
from pathlib import Path

import dotenv

import stockMonitor.misc

dotenv.load_dotenv("../../.env")
dotenv.load_dotenv("../.env")
SITE_NAME = "Дэшборд акций"

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = stockMonitor.misc.get_env_str(
    "DJANGO_SECRET_KEY", default="NotSecretKey"
)
DEBUG = stockMonitor.misc.get_env_str("DJANGO_DEBUG", default="True")
POSTGRES_USER = stockMonitor.misc.get_env_str(
    "POSTGRES_USER", default="postgres"
)
POSTGRES_PASSWORD = stockMonitor.misc.get_env_str(
    "POSTGRES_PASSWORD", default="postgres"
)
POSTGRES_DB = stockMonitor.misc.get_env_str("POSTGRES_DB", default="test")
POSTGRES_PORT = stockMonitor.misc.get_env_str("POSTGRES_PORT", default="5432")
ALLOWED_HOSTS = stockMonitor.misc.get_env_list(
    "DJANGO_ALLOWED_HOSTS", default="*"
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "rest_framework",
    "rest_framework_simplejwt",
    "django_rest_passwordreset",
    "corsheaders",
    "authentification.apps.AuthentificationConfig",
    "core.apps.CoreConfig",
    "stocks.apps.StocksConfig",
    "portfolio.apps.PortfolioConfig"
    "drf_spectacular",
    "django_celery_beat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1", "localhost"]
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }


ROOT_URLCONF = "stockMonitor.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR, BASE_DIR / "../" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "stockMonitor.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": "localhost",
        "PORT": POSTGRES_PORT,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation"
        ".UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".NumericPasswordValidator",
    },
]
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "StockMonitor API",
    "DESCRIPTION": "StockMonitor bro",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

CORS_ALLOWED_ORIGINS = stockMonitor.misc.get_env_list(
    "DJANGO_CORS_HOSTS", "http://localhost:3000"
)

SPECTACULAR_SETTINGS = {
    "TITLE": "StockMonitor API",
    "DESCRIPTION": "StockMonitor bro",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
}
AUTH_USER_MODEL = "core.User"

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

PARSING_INTERVAL = 5


EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "../sent_emails"

EMAIL_ADDRESS = "from_email@stockmonitor.ru"

REDIS_PASSWORD = stockMonitor.misc.get_env_str(
    "REDIS_PASSWORD", default="NotSecretPassword"
)
CELERY_BROKER_URL = "redis://127.0.0.1:6379"  # ubuntu
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_result_serializer = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_cache_backend = "django-cache"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"
