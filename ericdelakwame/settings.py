import os
import environ

env = environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.gis',
    'django.contrib.postgres',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_gis',
    'crispy_forms',
    'djmoney',
    'social_django',
    'phonenumber_field',
    'mapwidgets',
    'django_filters',
    'multiselectfield',
    'taggit',
    'taggit_serializer',
    'pwa',
    'hitcount',
    'fcm_django',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

]

ROOT_URLCONF = 'ericdelakwame.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'ericdelakwame.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'ericdelakwame_db',
        'USER': 'ericdelakwamedb_user',
        'PASSWORD': 'nemesis123',
        'PORT': '',
        'HOST': 'localhost'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# GOOGLE MAPS
GOOGLE_MAP_API_KEY = env("GOOGLE_MAP_API_KEY")

# MAPWIDGETS

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 12),
        ("mapCenterLocationName", "Accra"),
        ("GooglePlaceAutocompleteOptions", {
         'componentRestrictions': {'country': 'gh'}}),
        ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY": GOOGLE_MAP_API_KEY
}

# CRISPY-FORMS
CRISPY_FORMS_TEMPLATE = 'bootstrap4'

# AUTH_USER
AUTH_USER_MODEL = 'accounts.User'

LOGIN_URL = '/accounts/login'
# REDIRECT_URLS
LOGIN_REDIRECT_URL = 'accounts:profile'


# CELERY
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Accra'
CELERY_BEAT_SCHEDULE = {}

SENDGRID_API_KEY = env('SENDGRID_API_KEY')

TWILIO_ACCOUNT_SID = env('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = env('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = env('TWILIO_NUMBER')

# SOCIAL DJANGO
SOCIAL_AUTH_TWITTER_LOGIN_URL = 'accounts:profile'
SOCIAL_AUTH_LOGIN_URL = 'accounts:profile'
LOGIN_URL = 'accounts:profile'

AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',

)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)


SOCIAL_AUTH_USER_MODEL = 'accounts.User'

SOCIAL_AUTH_JSONFIELD_ENABLED = True

SOCIAL_AUTH_URL_NAMESPACE = 'social'


# SOCIAL CREDENTIALS
# ******************
# GOOGLE
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('GOOGLE_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('GOOGLE_CLIENT_SECRET')
# TWITTER
SOCIAL_AUTH_TWITTER_KEY = env('TWITTER_API_KEY')
SOCIAL_AUTH_TWITTER_SECRET = env('TWITTER_API_SECRET')
# FACEBOOK
SOCIAL_AUTH_FACEBOOK_KEY = env('FACEBOOK_ID')
SOCIAL_AUTH_FACEBOOK_SECRET = env('FACEBOOK_SECRET')


TAGGIT_CASE_INSENSITIVE = True
# FIREBASE_APP = initialize_app()
# GOOGLE_APPLICATION_CREDENTIALS = '/home/eric/projects/admjson/africandesign-f89bf-firebase-adminsdk-wx5uh-0443951341.json'

FCM_DJANGO_SETTINGS = {
    # default: _('FCM Django')
    "APP_VERBOSE_NAME": "africandesignmatters",
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": False,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": False,
}


# CART
CART_SESSION_ID = 'cart'

ADMINS = [('Eric', 'ericdelakwame@gmail.com')]
SITE_ID = 1


# EMAIL
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# SLACK STUFF

SLACK_CLIENT_ID = env('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = env('SLACK_CLIENT_SECRET')
SLACK_SIGNING_SECRET = env('SLACK_SIGNING_SECRET')

SLACK_LOGIN_OAUTH_REDIRECT_URL = "/accounts/profile"
SLACK_INSTALL_OAUTH_REDIRECT_URL = "/accounts/profile"
SLACK_AUTH_TOKEN = env('SLACK_AUTH_TOKEN')
SLACK_APP_TOKEN = env('SLACK_APP_TOKEN')


# CACHES
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# PWA
PWA_APP_NAME = 'ericdelakwame'
PWA_APP_DESCRIPTION = "EDK Cloud Works" 
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/' 
PWA_APP_ORIENTATION = 'any' 
PWA_APP_START_URL = '/' 
PWA_APP_STATUS_BAR_COLOR = 'default' 
PWA_APP_ICONS = [{'src': '/static/images/my_app_icon.png', 'sizes': '160x160'}]
PWA_APP_ICONS_APPLE = [
    {'src': '/static/images/my_apple_icon.png', 'sizes': '160x160'}]
PWA_APP_SPLASH_SCREEN = [{'src': '/static/images/icons/splash-640x1136.png', 'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'}] 
PWA_APP_DIR = 'ltr' 
PWA_APP_LANG = 'en-US'
