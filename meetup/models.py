from django.db import models
from django.contrib.auth.models import User


class CreatedUpdatedModel(object):
    created = models.DateTime(auto_now_add=True)
    updated = models.DateTime(auto_now=True)


class Talk(models.Model, CreatedUpdatedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    speaker = models.ForeignKey(User)
    meetup = models.ForeignKey('Meetup')
    slides = models.URLField()


class Meetup(models.Model, CreatedUpdatedModel):
    when = models.DateTimeField()
    venue = models.ForeignKey('Venue')


class Venue(models.Model, CreatedUpdatedModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Speaker(models.Model, CreatedUpdatedModel):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=255)
    bio = models.TextField()
    url = models.URLField()
