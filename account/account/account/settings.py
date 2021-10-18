"""
Django settings for account project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
# from authentication.common_shared.sensitive_data import (
#     DbPassword,
#     DbUsername,
#     DB_HOST,
#     JWT_AUDIENCE,
#     JWT_ISSUER,
#     FIELD_ENCRYPTION_MODEL_KEY
# )

# Build paths inside the project like this: BASE_DIR / 'subdir'.


BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'JWT_SECURITY_TOKEN'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'encrypted_model_fields',
    'authentication',
    'coverage',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
]

# cors headers allowed hosts. This enables calls from localhost
# ALLOWED_HOSTS = []
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

ROOT_URLCONF = 'account.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'account.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# uncomment to create test database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


FIELD_ENCRYPTION_KEY = os.environ.get('FIELD_ENCRYPTION_KEY')
# FIELD_ENCRYPTION_KEY = FIELD_ENCRYPTION_MODEL_KEY
# comment current DB settings to create test DB
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            'name': '3vial',
            # 'host': DB_HOST,
            'host': os.environ.get('DB_HOST'),
            'username': os.environ.get('DB_USERNAME'),
            'password': os.environ.get('DB_PASSWORD'),
            # username and password for development if environment variables are not set
            # 'username': DbUsername,
            # 'password': DbPassword,
            'authMechanism': 'SCRAM-SHA-1'

        }
    }
}
# DB for testing
import sys

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""
JWT authentication currently using only the admin user in Django 
Important: Django admin username must be auth0user
"""

JWT_AUTH = {
    'JWT_PAYLOAD_GET_USERNAME_HANDLER':
        'authentication.common_shared.utils.auth0user',
    'JWT_DECODE_HANDLER':
        'authentication.common_shared.utils.jwt_decode_token',
    'JWT_ALGORITHM': 'RS256',
    # 'JWT_AUDIENCE': JWT_AUDIENCE,
    'JWT_AUDIENCE': os.environ.get('JWT_AUDIENCE'),
    # 'JWT_ISSUER': JWT_ISSUER,
    'JWT_ISSUER': os.environ.get('JWT_ISSUER'),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}
