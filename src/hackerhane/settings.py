"""
Django settings for Hackerhane project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ADMINS = (
     ('Elif T. Kus', 'elifkus@gmail.com'),
)

MANAGERS = ADMINS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common',
    'accounting',
    'members',
    'membership',
    'bootstrapform',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.linkedin',
    #'allauth.socialaccount.providers.openid',
    #'allauth.socialaccount.providers.stackexchange',
    #'allauth.socialaccount.providers.twitter',
    'django.contrib.sites', #added for allauth
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hackerhane.urls'

WSGI_APPLICATION = 'hackerhane.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'members.HsUser'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug", 
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

DATE_FORMAT = 'j N Y'

#allauth settings
ACCOUNT_AUTHENTICATION_METHOD = "email"

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION ="required"

ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Ist Hs] "

ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL ="/"
ACCOUNT_SIGNUP_FORM_CLASS = 'members.forms.SignupForm'
#A string pointing to a custom form class (e.g. 'myapp.forms.SignupForm') that is used during signup to ask the user for additional input (e.g. newsletter signup, birth date). This class should implement a 'save' method, accepting the newly signed up user as its only parameter.
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
#ACCOUNT_USER_DISPLAY (=a callable returning user.username)
#A callable (or string of the form 'some.module.callable_name') that takes a user as its only argument and returns the display name of the user. The default implementation returns user.username.
ACCOUNT_USERNAME_MIN_LENGTH = 5
#ACCOUNT_USERNAME_BLACKLIST (=[])
ACCOUNT_USERNAME_REQUIRED = False
#ACCOUNT_PASSWORD_INPUT_RENDER_VALUE (=False)
#render_value parameter as passed to PasswordInput fields.
ACCOUNT_PASSWORD_MIN_LENGTH = 6
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_AUTO_SIGNUP = False
#Attempt to bypass the signup form by using fields (e.g. username, email) retrieved from the social account provider. If a conflict arises due to a duplicate e-mail address the signup form will still kick in.
#SOCIALACCOUNT_AVATAR_SUPPORT (= 'avatar' in settings.INSTALLED_APPS)
#Enable support for django-avatar. When enabled, the profile image of the user is copied locally into django-avatar at signup.
SOCIALACCOUNT_EMAIL_REQUIRED = ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_EMAIL_VERIFICATION = False

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = \
    { 'facebook':
        { 'SCOPE': ['email',],
          'AUTH_PARAMS': { 'auth_type': 'reauthenticate' },
          'METHOD': 'oauth2' ,
          'LOCALE_FUNC': lambda request: 'tr_TR'},
      'google':
        { 'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile', 
                    'https://www.googleapis.com/auth/userinfo.email'],
          'AUTH_PARAMS': { 'access_type': 'online' } }
    }
    
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/usr/local/virtualenvs/hs-members-server/logs/django.log',
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['logfile',],
            'level': 'INFO',
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['logfile'],
            'propagate': False,
        },
    }
}


try:
    from hackerhane.local_settings import *
except ImportError:
    pass