"""
Django settings for esr21_follow project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ETC_DIR = '/etc/'

SITE_ID = 40

REVIEWER_SITE_ID = 1

APP_NAME = 'esr21_follow'


LOGIN_REDIRECT_URL = 'home_url'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k@ob))o-hjpw(m#d&tgm83&1%k8dv&(jy&p-4c=sz7m8^bk)bh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'django_js_reverse',
    'simple_history',
    'multiselectfield',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_sync.apps.AppConfig',
    'edc_sync_files.apps.AppConfig',
    'edc_base.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_lab_dashboard.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_call_manager.apps.AppConfig',
    'esr21_subject.apps.AppConfig',
    'esr21_follow.apps.EdcAppointmentAppConfig',
    'esr21_follow.apps.EdcProtocolAppConfig',
    'esr21_follow.apps.EdcTimepointAppConfig',
    'esr21_follow.apps.EdcVisitTrackingAppConfig',
    'esr21_follow.apps.EdcSenaiteInterfaceAppConfig',
    'esr21_follow.apps.EdcLabAppConfig',
    'esr21_follow.apps.AppConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
    'edc_lab_dashboard.middleware.DashboardMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

ROOT_URLCONF = 'esr21_follow.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'esr21_follow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEVICE_ID = '99'
DEVICE_ROLE = 'CentralServer'

DASHBOARD_URL_NAMES = {
    'esr21_follow_listboard_url': 'esr21_follow:esr21_follow_listboard_url',
    'esr21_follow_book_listboard_url': 'esr21_follow:esr21_follow_book_listboard_url'

}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'esr21/base.html',
    'dashboard_base_template': 'esr21/base.html',
    'esr21_follow_listboard_template': 'esr21_follow/follow_listboard.html',
    }

LAB_DASHBOARD_URL_NAMES = {}

EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USB_VOLUME = None

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

if 'test' in sys.argv:

    class DisableMigrations:

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

