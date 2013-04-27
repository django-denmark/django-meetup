from django.contrib import admin

import models

admin.site.register(models.Meetup)
admin.site.register(models.Venue)
admin.site.register(models.Speaker)
admin.site.register(models.Talk)
admin.site.register(models.Profile)
admin.site.register(models.RSVP)
