from .base import *

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret =file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

env = environ.Env(
    DEBUG=(bool, False)
)


environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


SECRET_KEY = read_secret('Basicframe_Django_Secret_Key') # secretkey 수정

DEBUG = False

ALLOWED_HOSTS = ['*'] #모든 호스트를 허용

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django', # yml 파일과 이름 맞춰주기
        'USER': 'peter', # yml 파일과 이름 맞춰주기
        'PASSWORD': read_secret('Basicframe_MariaDB_Password'),  # maridb 비밀번호 수정
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}