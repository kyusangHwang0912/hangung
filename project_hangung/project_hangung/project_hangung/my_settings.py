# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = {
    'secret' : 'django-insecure-^i%ubd3j*h@t*s2qr2!ti9e#7m9de2y7grl)_t=*vc_9hva2kt'
}

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}