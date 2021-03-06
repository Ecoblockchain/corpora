# -*- coding: utf-8 -*-
"""
Django settings for corpora project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = eval(os.environ['DJANGO_ISNOT_PRODUCTION'])

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(' ')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'corpora',
    'corpus',
    'people',

    'storages',
    'djangobower',

    'sekizai',
    'compressor',
    'sass_processor',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware', # <= for caching entire site
    'django.middleware.locale.LocaleMiddleware',
    'corpora.middleware.LanguageMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware', # <= for caching entire site
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'corpora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'corpora.wsgi.application'


# STORAGES #
DEFAULT_FILE_STORAGE =      os.environ['FILE_STORAGE']
AWS_ACCESS_KEY_ID =         os.environ['AWS_ID']
AWS_SECRET_ACCESS_KEY =     os.environ['AWS_SECRET']
AWS_STORAGE_BUCKET_NAME =   os.environ['AWS_BUCKET']
AWS_QUERYSTRING_AUTH = False



# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# We use ansible to create the environment variables to use.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'], # TODO: Give this a better name?
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'], # TODO: Secure this!
        'HOST': os.environ['DATABASE_HOST'],           
        'PORT': '5432',
        }
    }

# All auth
AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
)
LOGIN_REDIRECT_URL = 'people:profile' # is there a more fool proof option?
ACCOUNT_ADAPTER = "people.adapter.PersonAccountAdapter"
SOCIALACCOUNT_ADAPTER = "people.adapter.PersonSocialAccountAdapter"
SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'], # Will require app approval for user_about_me access.
        'FIELDS': [ # see https://developers.facebook.com/docs/graph-api/reference/user/
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'locale',
            'timezone',
            'gender',
            'languages',
            'birthday'],
        #'LOCALE_FUNC': 'path.to.callable',
        'VERSION': 'v2.4'},
    'google':{
        'SCOPE': ['profile', 'email', 'https://www.googleapis.com/auth/plus.login'], # https://developers.google.com/identity/protocols/OAuth2
        'FIELDS': [ 
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'locale',
            'timezone',
            'gender',
            'languages',
            'birthday'],
    }
    }
ACCOUNT_AUTHENTICATION_METHOD="username_email"
ACCOUNT_EMAIL_REQUIRED=True

# These email settings should change for a production environment. Right now we're using G Suite.
# EMAIL_HOST=os.environ['EMAIL_HOST']
# EMAIL_HOST_USER=os.environ['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD=os.environ['EMAIL_HOST_PASSWORD']
# EMAIL_USE_SSL=True # move to deploy
# EMAIL_PORT=465 # Move to deploy

# Email
EMAIL_BACKEND = 'django_ses.SESBackend' # Use AWS Simple Email Service
AWS_SES_REGION_NAME = 'us-west-1'
AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'
DEFAULT_FROM_EMAIL = '"Te Hiku Support" <support@tehiku.nz>'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Site ID
SITE_ID = 1


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'mi'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Add support for IMPORTANT!!!!! languages
import django.conf.locale
EXTRA_LANG_INFO = {
    'mi': {
        'bidi': False, # right-to-left
        'code': 'mi',
        'name': 'Maori',
        'name_local': u'Māori',
    },
    'en_NZ': {
        'bidi': False, # right-to-left
        'code': 'en_NZ',
        'name': 'New Zealand English',
        'name_local': u'New Zealand English',
    },
}
LANG_INFO = dict(django.conf.locale.LANG_INFO.items() + EXTRA_LANG_INFO.items())
 
# update the language info
django.conf.locale.LANG_INFO = LANG_INFO

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    # ('en',    _('English')),
    ('mi',    _('Maori')),
    # ('en_NZ', _('New Zealand English')),
)
# LANGUAGE_COOKIE_NAME='corpora-language'

# LOCALE_PATHS = (
# We're making a local directory in each app and the project-app folder
#     os.path.join(BASE_DIR, 'locale'),
# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ['STATIC_PATH'] #os.path.join(BASE_DIR, 'public', 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ['MEDIA_PATH']

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'corpora/static')

BOWER_INSTALLED_APPS = {
    'jquery',
    'jquery-ui',
    'bootstrap',
    'opus-recorderjs',
    'components-font-awesome',
}

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, '...', 'static'),
# )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',

    # Additional finders
    'djangobower.finders.BowerFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',

)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '%s:%s'%(os.environ['DJANGO_MEMCACHED_IP'], os.environ['DJANGO_MEMCACHED_PORT']),
        'TIMEOUT': 300,
    }
}

# These may be required if caching the entire site.
# CACHE_MIDDLEWARE_ALIAS 
# CACHE_MIDDLEWARE_SECONDS
# CACHE_MIDDLEWARE_KEY_PREFIX


# DJANGO-COMPRESSOR SETTINGS
COMPRESS_PRECOMPILERS = (
    #('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
    #('text/stylus', 'stylus < {infile} > {outfile}'),
    #('text/foobar', 'path.to.MyPrecompilerFilter'),
)



import sys


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s -- %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
        },
        'testconsole': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '../../logs/django.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 10,  # 10 mb                        
        },      
        'celery': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '../../logs/celery.log',
            'formatter': 'simple',
            'maxBytes': 1024 * 1024 * 10,  # 10 mb            
        }
    },
    'loggers': {
        'django.test':{
            'handlers': ['testconsole'],
            'level': 'DEBUG',
            'propogate': True        
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'corpora': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propogate': True
        },
        'celery': {
            'handlers': ['celery', 'console'],
            'level': 'DEBUG',
            'propogate': True
        }
    }
}


