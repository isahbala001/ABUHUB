SECRET_KEY = '-ri3j9arn2w=yz_wgq2to(pt7uif^6f@gclptw0kch(b@eg%ho'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = []
MIDDLEWARE = []

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}