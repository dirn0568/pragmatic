
from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file


environ.Env.read_env(
    env_file= os.path.join(BASE_DIR, '.env')
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# 마리아db와 mysql은 비슷함 그래서 엔진에 mysql로 적은거임
# 마리아db는 3306포트를 사용함

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}