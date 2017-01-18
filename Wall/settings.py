# -*- coding:utf-8 -*- 
import os
from os import path 

SESSION_EXPIRE_AT_BROWSER_CLOSE=True

PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

SECRET_KEY = '#24dk%=uz8dx9(r&4$l%dd@qj9e()6^y8ezwpg!-0i*k0&kp)z'

DEBUG = True

LOGIN_URL = '/fundpart/userlogin/'

IME_ZONE = 'Asia/Shanghai'

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
    # 'rest_framework_swagger',
    # 'xadmin',
    # 'crispy_forms',
    # 'reversion',
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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
            ],
        },
    },
]


WSGI_APPLICATION = 'Wall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

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


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True
USE_TZ = True




STATIC_URL = '/static/'

STATIC_ROOT = path.join(PROJECT_ROOT, 'static').replace('\\', '/')

MEDIA_URL = '/media/'

MEDIA_ROOT = path.join(PROJECT_ROOT, 'media').replace('\\', '/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



REST_FRAMEWORK_DOCS = {
    'HIDE_DOCS': False
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 8,
    'FILTER_BACKEND': 'rest_framework.filters.DjangoFilterBackend',
    'DATETIME_FORMAT': ("%Y-%m-%d %H:%M:%S"),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    )
}




