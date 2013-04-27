from django.conf.urls import patterns, url
from .views import MeetupDetail, MeetupList, MeetupCreate

urlpatterns = patterns(
    '',
    url(r'^$', MeetupList.as_view(), name="meetup-list"),
    url(r'^(?P<pk>\d+)/$', MeetupDetail.as_view(), name="meetup-detail"),
    url(r'^new-meetup/$', MeetupCreate.as_view(), name="meetup-create"),
)
