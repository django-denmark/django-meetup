from django.conf.urls import patterns, url
from .views import MeetupDetail, MeetupList

urlpatterns = patterns(
    '',
    url(r'^$', MeetupList.as_view(), name="meetup-list"),
    url(r'(?P<pk>\d+)/$', MeetupDetail.as_view(), name="meetup-detail"),
)
