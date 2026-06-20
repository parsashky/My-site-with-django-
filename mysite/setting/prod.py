from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2=$e=qrfz%7e&9wd^(9rl2rkiq5+^xel)xx5!k6yj)&l3+7kah'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['my-site-with-django-1.onrender.com', 'localhost', '127.0.0.1']

INSTALL_APPS = []

# sites framwork
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_ROOT  = BASE_DIR / 'media'
STATIC_ROOT  = BASE_DIR / 'static'
STATICFILES_DIRS =[
    BASE_DIR / 'statics',
]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True