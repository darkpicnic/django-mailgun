from django.conf import settings

MAILGUN_URL = getattr(settings, 'MAILGUN_URL', None)
MAILGUN_APP = getattr(settings, 'MAILGUN_APP', None)
MAILGUN_KEY = getattr(settings, 'MAILGUN_KEY', None)
FROM_EMAIL  = getattr(settings, 'MAILGUN_FROM_EMAIL', None)
DEBUG_MODE  = getattr(settings, 'MAILGUN_DEBUG_MODE', False)
ADMINS 	    = getattr(settings, 'MAILGUN_ADMINS', settings.ADMINS)