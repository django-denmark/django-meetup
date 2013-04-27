from django.contrib import admin

from .models import Meetup, Venue, Speaker, Talk

admin.site.register(Meetup)
admin.site.register(Venue)
admin.site.register(Speaker)
admin.site.register(Talk)
