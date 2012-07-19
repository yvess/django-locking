from django.conf import settings

MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')
ADMIN_URL = getattr(settings, 'ADMIN_URL', '/admin/')
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')
