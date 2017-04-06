# -*- coding:utf-8 -*- 
import os



SESSION_EXPIRE_AT_BROWSER_CLOSE=True



SECRET_KEY = '#24dk%=uz8dx9(r&4$l%dd@qj9e()6^y8ezwpg!-0i*k0&kp)z'

DEBUG = True

LOGIN_URL = '/fundpart/userlogin/'

MANAGERS = (
     ('ccyutaotao', '2622355408@qq.com'),
)

ALLOWED_HOSTS = [
 'localhost',
]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'FundPart',
    'rest_framework',
    'rest_framework_docs',
    'djcelery',
    'rest_framework_swagger'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Wall.urls'

WSGI_APPLICATION = 'Wall.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Wall',
        'USER': 'root',
        'PASSWORD': '5201314ytt!@',
        'HOST':'',
        'PORT':'3306'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media').replace('\\', '/')

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates').replace('\\', '/'),
    os.path.join(PROJECT_ROOT, 'Fundpart/templates/Fundpages').replace('\\', '/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 8,
    'FILTER_BACKEND': 'rest_framework.filters.DjangoFilterBackend',
    'DATETIME_FORMAT': ("%Y-%m-%d %H:%M:%S"),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES':(
         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
    ),
}

REST_FRAMEWORK_DOCS = {
    'HIDE_DOCS': False
}

BROKER_URL = 'redis://127.0.0.1:6379/0'
BROKER_TRANSPORT = 'redis'
