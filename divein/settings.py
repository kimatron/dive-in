# """
# Django settings for divein project.

# Generated by 'django-admin startproject' using Django 4.2.10.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/4.2/ref/settings/

# """

from pathlib import Path
import os
import sys
import dj_database_url

if os.path.isfile('env.py'):
    import env  # noqa: F401

# Now use os.environ.get() for all environment variables

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


SECRET_KEY = os.environ.get("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ

ALLOWED_HOSTS = [
    '.herokuapp.com',
    '127.0.0.1',
    'localhost',
    '.codeinstitute-ide.net',  # CodeInstitute workspace URLs
    '8000-kimatron-divein-s6fk5u1m3yn.ws.codeinstitute-ide.net'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'crispy_bootstrap5',
    'blog',
    'django_summernote',
    'cloudinary',
    'about',
]

CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')
CLOUDINARY_SECURE = True

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'divein.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'divein.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

CSRF_TRUSTED_ORIGINS = [
    'https://*.codeinstitute-ide.net',
    'https://*.gitpod.io',
    'https://*.herokuapp.com'
]
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# ACCOUNT_EMAIL_VERIFICATION = 'none'

# Email Settings
# if 'DEVELOPMENT' in os.environ:
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# else:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # This is literally the string 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

# Django allauth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_USER_DISPLAY = lambda user: user.get_username()
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_ADAPTER = 'blog.adapters.CustomAccountAdapter'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Dive In Blog - '  # Customize email subject
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
# Make sure it's set again here
SERVER_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')


# Add these for debugging email issues
EMAIL_DEBUG = True
EMAIL_FAIL_SILENTLY = False

# Email logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    "https://fonts.googleapis.com",
    "https://cdn.jsdelivr.net",
    "https://cdnjs.cloudflare.com",
)
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "https://cdn.jsdelivr.net",
    "https://cdnjs.cloudflare.com",
)
CSP_FONT_SRC = (
    "'self'",
    "https://fonts.gstatic.com",
    "https://cdn.jsdelivr.net",
    "https://cdnjs.cloudflare.com",
)
CSP_IMG_SRC = (
    "'self'",
    "https:",
    "data:",
    "https://res.cloudinary.com",
)
CSP_CONNECT_SRC = ("'self'",)

# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = 'DENY'
# SECURE_HSTS_SECONDS = 31536000  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True