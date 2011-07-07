from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home', name='home'),
    url(r'^events/', 'events.views.index'),
    url(r'^calais/', 'events.views.calais_test'),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html' }),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url('^_ah/warmup$', 'djangoappengine.views.warmup'),
)
