from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="my_logout"),
    url(r'^', include('project.project.meetup.urls', namespace='meetup', app_name='meetup')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
)

urlpatterns += patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)
