from config.settings.common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^@792lzizp*h=rm2kq$fi-b=-!y^p!a$ee(=*qw%&p=)gkfzhs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = ()
