"""
Django settings for vote4film project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/latest/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/latest/ref/settings/
"""
import sys

import environ
from django.core.exceptions import ImproperlyConfigured
from xdg import xdg_config_home

from vote4film import __version__

settings_path = environ.Path(__file__) - 1
django_app = settings_path - 1
repo_root = django_app - 1


# Great setup for local developers, just need to enable DEBUG in local.env
env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "lih*)#c#npi*(tgw8xs-@4a-%k*1tnd4uqo)zy!rzzx5sc#-+d"),
    ADMIN=(tuple, []),  # Tuple of ONE admin (name, email)
    ALLOWED_HOSTS=(list, []),
    STATIC_URL=(str, "/static/"),  # URL path that server will server static files from
    STATIC_ROOT=(str, None),  # Collect static files here
    DATABASE=(str, "sqlite:///" + repo_root("db.sqlite3")),
    OMDB_API_KEY=(str, ""),  # REQUIRED if omdb is used
    SENTRY_DSN=(str, ""),  # REQUIRED if sentry is used
    SENTRY_TRACE_RATE=(float, 0.01),
)


if (xdg_config_home() / "vote4film/local.env").exists():
    config_file = str(
        environ.Path(xdg_config_home() / "vote4film/local.env", required=True)
    )
else:
    config_file = repo_root("local.env", required=True)

# Read environment configuration (it must exist even for local developers)
try:
    environ.Env.read_env(config_file)
except ImproperlyConfigured:
    print("-" * 80)
    print("Are you a developer running this locally?")
    print('You must create local.env in repository root with "DEBUG=on" inside.')
    print("-" * 80)
    sys.exit(1)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")
ADMINS = [env("ADMIN")]  # Emailed on 500 error


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(levelname)s %(asctime)s {request:%(request_uuid)s} {user:%(request_user)s} "
                "%(module)s %(process)d %(thread)d %(message)s"
            )
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"},
        "vote4film_context": {"()": "vote4film.log.global_context_filter"},
    },
    "handlers": {
        "syslog": {
            "level": "DEBUG",
            "class": "logging.handlers.SysLogHandler",
            "address": "/dev/log",
            "filters": ["require_debug_false", "vote4film_context"],
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "filters": ["require_debug_true", "vote4film_context"],
            "formatter": "simple",
        },
    },
    "loggers": {
        "": {"level": "DEBUG", "handlers": ["syslog", "console"], "propagate": True}
    },
}

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "calender",
    "films",
    "schedule",
    "votes",
    "web",
]

if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = [
    "vote4film.middleware.add_request_logging_context",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "vote4film.middleware.add_user_logging_context",
    "vote4film.middleware.login_required_middleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1", "::1"]  # 127.0.0.1 used by django-debug-toolbar

ROOT_URLCONF = "vote4film.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "calender.context_processors.next_event_register_url",
                "votes.context_processors.is_vote_available",
            ]
        },
    }
]

LOGIN_URL = "web:login"
LOGIN_REDIRECT_URL = "web:home"
LOGOUT_REDIRECT_URL = "web:login"

WSGI_APPLICATION = "vote4film.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {"default": env.db("DATABASE")}
CONN_MAX_AGE = 60 * 60 * 24  # Persist DB connections for one day

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = (
    "vote4film.auth.UsernameAsEmailBackend",
    "django.contrib.auth.backends.ModelBackend",
)

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = env("STATIC_URL")
STATIC_ROOT = env("STATIC_ROOT")

# Security
SILENCED_SYSTEM_CHECKS = ["security.W004"]  # SECURE_HSTS_SECONDS managed by Nginx
if DEBUG:
    # Ignore these locally
    SILENCED_SYSTEM_CHECKS += [
        "security.W008",  # SECURE_SSL_REDIRECT
        "security.W012",  # SESSION_COOKIE_SECURE
        "security.W016",  # CSRF_COOKIE_SECURE
        "security.W018",  # DEBUG
        "security.W020",  # ALLOWED_HOSTS
    ]


# Web security
X_FRAME_OPTIONS = "DENY"  # (Nginx does it also)
SECURE_CONTENT_TYPE_NOSNIFF = True  # (Nginx does it also)
SECURE_BROWSER_XSS_FILTER = True  # (Nginx does it also)
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 365 * 24 * 60 * 60  # 1 year long login sessions
SESSION_COOKIE_HTTPONLY = True  # Do not let JavaScript read the Session cookie
# The development server uses HTTP
if not DEBUG:
    CSRF_COOKIE_SECURE = True  # Avoid sending over HTTP
    SESSION_COOKIE_SECURE = True  # Avoid sending over HTTP
    SECURE_SSL_REDIRECT = True  # Redirect HTTP -> HTTPS (Nginx does it also)


# Local security
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o550
FILE_UPLOAD_PERMISSIONS = 0o640


# Other
OMDB_API_KEY = env("OMDB_API_KEY")
if env("SENTRY_DSN"):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=env("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        send_default_pii=True,
        attach_stacktrace=True,
        request_bodies="medium",
        traces_sample_rate=env("SENTRY_TRACE_RATE"),
        _experiments={"auto_enabling_integrations": True},
        release=f"vote4film@{__version__}",
    )
