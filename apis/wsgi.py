"""
WSGI config for apis project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/
"""
import os
from pathlib import Path

import sys

# # os.environ.setdefault("DJANGO_CONFIGURATION", "Production")
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR / "apis"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apis.config.local")

from django.core.wsgi import get_wsgi_application  # noqa
application = get_wsgi_application()
