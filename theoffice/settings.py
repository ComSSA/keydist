# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('THEOFFICE_SECRET_KEY')
POSTMARK_API_KEY = os.environ.get('THEOFFICE_POSTMARK_KEY')
POSTMARK_SENDER = os.environ.get('THEOFFICE_POSTMARK_SENDER')

DEBUG = os.environ.get('THEOFFICE_DEBUG', False) == 'True'
TEMPLATE_DEBUG = DEBUG

# Application definition
INSTALLED_APPS = (
    # Django applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',

    # Custom applications
    'home',
    'accounts',
    'keys',
    'policy',

    # Template tags
    'tags',

    # Third party applications
    'south',
    'lockout',
    'bootstrap3',
    'pagedown',
    'markdown_deux',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'lockout.middleware.LockoutMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'theoffice.urls'
WSGI_APPLICATION = 'theoffice.wsgi.application'


DBENV = os.environ.get('THEOFFICE_DB_ENV')

if DBENV == 'dev':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
elif DBENV == 'deploy':
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('THEOFFICE_DB_BACKEND'),
            'NAME': os.environ.get('THEOFFICE_DB_NAME'),
            'USER': os.environ.get('THEOFFICE_DB_USER'),
            'PASSWORD': os.environ.get('THEOFFICE_DB_PASSWORD'),
            'HOST': os.environ.get('THEOFFICE_DB_HOST'),
            'PORT': os.environ.get('THEOFFICE_DB_PORT'),
        }
    }
else:
    raise Exception('Invalid database environment: %s' % DBENV)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-au'
TIME_ZONE = 'Australia/Perth'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

AUTH_USER_MODEL = 'accounts.KeydistUser'

# Postmark Emails
EMAIL_BACKEND = 'postmark.backends.PostmarkBackend'

# Proxy stuff
USE_X_FORWARDED_HOST = True

# Customised django.contrib.messages for bootstrap
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# pytidyclub settings.
TIDYCLUB_API_ID = os.environ.get('THEOFFICE_TIDYCLUB_API_KEY')
TIDYCLUB_API_SECRET = os.environ.get('THEOFFICE_TIDYCLUB_API_SECRET')
