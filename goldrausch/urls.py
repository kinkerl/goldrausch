from django.conf.urls.defaults import patterns, include, url
import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'main.views.index'),
	url(r'^update/(?P<boardid>\d+)/(?P<eventid>\d+)/(?P<statuscode>\d+)/(?P<secret>.*)', 'main.views.update'),
	url(r'^overview', 'main.views.overview'),

	(r'^admin/doc/', include('django.contrib.admindocs.urls')), # admin documentation
	url(r'^admin/', include(admin.site.urls)),   #admn interface
	(r'^grappelli/', include('grappelli.urls')), #new admin skin
)

#serving images, assets and doc in debug-mode
if settings.DEBUG: 
	urlpatterns += patterns('',
		url(r'^admin/doc/', include('django.contrib.admindocs.urls')), # admin documentation
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.MEDIA_ROOT,
		}),
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.STATIC_ROOT,
		}),
		#view the sphinx generated doc with the django build in server
		url(r'^doc/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': '../doc/_build/html/',
		}),
	)
