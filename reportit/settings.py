"""
Django settings for reportit project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#so_!xgo2=9p4712=y*he&*z7=*nzlikc^@zv-rsl-%n%@=gyv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'webpage.apps.WebpageConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     # used for third party login
     #'widget_tweaks',
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # used for third party login
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'reportit.urls'

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
                # used for third party login
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


WSGI_APPLICATION = 'reportit.wsgi.application'

#add for third party login
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASE_URL = 'postgres://tqohuspthbqznq:ab094f88f696ac1fd5a70e803f07f9b3b46e821a6816fb5bae9042490dbca647@ec2-184-73-174-10.compute-1.amazonaws.com:5432/d192pbou671pol'
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'client_encoding': 'UTF8',
        'default_transaction_isolation': 'read committed'
    }
}

DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)


# Login redirect
LOGIN_REDIRECT_URL = '/account/dashboard'

#default URL used for third paty login d\
SOCIAL_AUTH_LOGIN_ERROR_URL = '/redicrect_error/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/oauthinfo/'
#SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/account/dashboard'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_USERNAME_FORM_URL = '/login-form/'
SOCIAL_AUTH_USERNAME_FORM_HTML = '/webpage/templates/webpage/reporterSignup.html'

#SOCIAL_AUTH_USER_MODEL = 'webpage.Reporter'

#used for third party login
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '526390079783-65f89qmpk4120cqgpps2pm4mvlth3f1f.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'UkY8l1aM01Y2cmJyRsSmNH2b'

SOCIAL_AUTH_FACEBOOK_APP_KEY = '166948077223824'
SOCIAL_AUTH_FACEBOOK_APP_SECRET = '9e7934e9cd44fe6967b9e87f4d01b8aa'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ALLOWED_HOSTS = ['0.0.0.0']
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'webpage/static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


#enable email function
if DEBUG:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'johnnyforproject@gmail.com'
    EMAIL_HOST_PASSWORD = '19941214'
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'ReportIt Team'


