"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.getenv('DJANGO_ENV', 'dev')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.{}".format(env))

application = get_wsgi_application()
