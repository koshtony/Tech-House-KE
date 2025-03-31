"""
Django settings for tech_house project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'preventconcurrentlogins',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'ecommerce',
    'general',
    'manager',
    'rest_framework',
    'django_htmx',
    'debug_toolbar', 
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware'
]

ROOT_URLCONF = 'tech_house.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ecommerce.context_processors.cart',
                'ecommerce.context_processors.show_products',
                'ecommerce.context_processors.show_org_profile',
                
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
	  'allauth.account.auth_backends.AuthenticationBackend',
    ]


WSGI_APPLICATION = 'tech_house.wsgi.application'

USE_THOUSAND_SEPARATOR = True

INTERNAL_IPS = [                                               # <-- NEW
    '127.0.0.1',                                               # <-- NEW
]                                                              # <-- NEW

def show_toolbar(request):                                     # <-- NEW
    return True                                                # <-- NEW 

DEBUG_TOOLBAR_CONFIG = {                                       # <-- NEW
    "SHOW_TOOLBAR_CALLBACK" : lambda r: False,                    # <-- NEW
}                                                              # <-- NEW

if DEBUG:                                                      # <-- NEW
    import mimetypes                                           # <-- NEW          
    mimetypes.add_type("application/javascript", ".js", True)


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.getenv('POSTGRES_DB'),
       'USER': os.getenv('POSTGRES_USER'),
       'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
       'HOST': os.getenv('PGHOST'),
       'PORT': os.getenv('PGPORT'),
   }
}






# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STORAGES = {
    # ...
    "default":{
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
    "mediafiles": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, 'general/static')
STATIC_URL = '/static/'


MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = ['https://tech-house-ke-production.up.railway.app']

CSRF_FAILURE_VIEW = 'ecommerce.views.csrf_failure_403'


LOGIN_REDIRECT_URL = 'eco-shop'
LOGOUT_REDIRECT_URL = 'eco-shop'


SOCIALACCOUNT_PROVIDERS = {
    
    'google': {
        'APP': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID'),
            'secret': os.getenv('GOOLGE_SECRET_KEY'),
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
    
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']
ACCOUNT_LOGIN_METHOD = 'email'
