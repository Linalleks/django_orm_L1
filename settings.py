from decouple import config

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = config('SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
