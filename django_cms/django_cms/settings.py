"""
Django settings for django_cms project.

Generated by 'django-admin startproject' using Django 1.8.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
gettext = lambda s: s

DATA_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd3=9i-msen!+6yrh^qx4ces#(a+d&i3j-o0#f-v3e5fp9-ob8q'

#from djangocms_text_ckeditor.settings import CKEDITOR_SETTINGS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'cristianalecu007.pythonanywhere.com']


# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_link',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    
    'aldryn_style',
    'mptt', 
    'aldryn_bootstrap3',
	'django_cms',
    'widget_tweaks',
	
	'allauth',
    'allauth.account',
    'allauth.socialaccount',
#     'allauth.socialaccount.providers.facebook',
#     'allauth.socialaccount.providers.google',
#     'allauth.socialaccount.providers.openid',
#     'allauth.socialaccount.providers.linkedin',
#     'allauth.socialaccount.providers.linkedin_oauth2',
    'financiar',
)

LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'django_cms.urls'

WSGI_APPLICATION = 'django_cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Bucharest'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'django_cms', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'django_cms', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('English')),
	('fr', gettext('French')),
	('ro', gettext('Romanian')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('English'),
            'fallbacks': ['ro'],
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
		{
			'code': 'fr',
			'name': gettext('French'),
			'fallbacks': ['en'],
			'redirect_on_fallback': True,
			'public': True,
			'hide_untranslated': False,
		},
		{
			'code': 'ro',
			'name': gettext('Romanian'),
			'fallbacks': ['en'],
			'redirect_on_fallback': True,
			'public': True,
			'hide_untranslated': False,
		},
    ],
    'default': {
		'fallbacks': ['en', 'fr', 'ro'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('dashboard.html', 'Dashbard'),
    ('tables.html', 'Tables'),
    ('flotchart.html', 'Flotcharts'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
 
# CKEDITOR_SETTINGS = {
# 	# 'languuage': '{{ language }}',
# 	# 'toolbar': 'CMS',
# 	# 'toolbar_CMS': [
# 	# 	['Undo', 'Redo'],
# 	# 	...
# 	# ],
#     'stylesSet': [
# 		{
# 			'name': 'Page Header H1',
# 			'element': 'h1',
# 			'attributes': {
# 				'class': 'page-header',
# 			}
# 		},
# 		{
# 			'name': 'Page Header H2',
# 			'element': 'h2',
# 			'attributes': {
# 				'class': 'page-header',
# 			}
# 		},
# 		{
# 			'name': 'Page Header H3',
# 			'element': 'h3',
# 			'attributes': {
# 				'class': 'page-header',
# 			}
# 		}
#     ],
# }

