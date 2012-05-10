# settings specific to the dev machine
# eg DATABASES, MEDIA_ROOT, etc
# You can completely override settings in settings.py 
# or even modify them eg:

# Due to how python imports work, this won't cause a circular import error
from settings import INSTALLED_APPS, MIDDLEWARE_CLASSES, LOCALE_PATHS

#setup debug toolbar on dev
INSTALLED_APPS += ("debug_toolbar",)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)


TEMPLATE_DIRS = (
	'/home/desch/devel/goldrausch/goldrausch/main/templates'
)

MEDIA_ROOT = '/home/desch/devel/goldrausch/goldrausch/media'
MEDIA_URL = '/media/'

STATIC_ROOT = '/home/desch/devel/goldrausch/goldrausch/static/'
STATIC_URL = '/static/'

#Path to search for the compiled(!) gettext Translations
LOCALE_PATHS += ('/home/desch/devel/goldrausch/goldrausch/locale', )

