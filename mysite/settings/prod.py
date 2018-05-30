from mysite.settings.base import *

# override settings for production

DEBUG = False

ALLOWED_HOSTS = ['thegreatest.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd62r1j5m7aq6t2',
        'USER': 'tueabssgdrsmnp',
        'PASSWORD': '82fd57f56d30ac67b49bab9ae7b55c64a6323c359abe786561999f831db76037',
        'HOST': 'ec2-54-235-206-118.compute-1.amazonaws.com',
        'PORT': '5432',
    },
}

SECRET_KEY = "SLUJ3p*rx_6UTa*?A2*YJmDv2C*j_e_z+8EXw+-XM&"

ADMINS = [('Valeriy', 'valeriykundas@gmail.com')]
MANAGERS = ADMINS