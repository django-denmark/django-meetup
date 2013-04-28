from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'^$', views.MeetupList.as_view(), name="meetup-list"),

    url(r'^meetups/(?P<pk>\d+)/$',
        views.MeetupDetail.as_view(), name="meetup-detail"),

    url(r'^meetups/new/$', views.MeetupCreate.as_view(), name="meetup-create"),

    url(r'^venues/$',
        views.VenueList.as_view(), name="venue-list"),

    url(r'^venues/(?P<pk>\d+)/$',
        views.VenueDetail.as_view(), name="venue-detail"),

    url(r'^venues/new/$', views.VenueCreate.as_view(), name="venue-create"),
)
