"""
Django settings for AIBH project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2ug_-g#i8^06j)k4!8al(wi7g5jp4vc7b2@3(u&&eg&x%^n)5v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aibh',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AIBH.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'AIBH.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'aibh/static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'aibh/media')


# settings.py
import os




# settings.py

# PayPal settings
PAYPAL_CLIENT_ID = 'votre_client_id_paypal'
PAYPAL_CLIENT_SECRET = 'votre_client_secret_paypal'
PAYPAL_API_URL = 'https://api-m.paypal.com'  # Utilisez 'https://api-m.sandbox.paypal.com' pour les tests




# settings.py

# Coinbase settings
COINBASE_API_KEY = 'votre_clé_api_coinbase'
COINBASE_API_URL = 'https://api.commerce.coinbase.com'  # L'URL de l'API Coinbase


# settings.py

# Clés API et Tokens pour les paiements
PAYDUNYA_TEST_PUBLIC_KEY = 'test_public_Yg90Qhzh6ftM4vBPNuIUieqhvMI'
PAYDUNYA_TEST_PRIVATE_KEY = 'test_private_Yus2UsJDipCwDZcaXP0P8bAtin2'
PAYDUNYA_TEST_TOKEN = 'soqi6kFyHP7FK4lbXXdA'

PAYDUNYA_PROD_PUBLIC_KEY = 'live_public_qkB1Hzakjxw9nzqh7AzfFII94At'
PAYDUNYA_PROD_PRIVATE_KEY = 'live_private_H3zWujFidmgjJerkVyHzOeOHuQg'
PAYDUNYA_PROD_TOKEN = 'xDDELzAQFzracZ5RKsFu'
