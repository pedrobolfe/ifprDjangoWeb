"""
WSGI config for pratica_sistema_viagem_2b project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pratica_sistema_viagem_2b.settings')

application = get_wsgi_application()
