from django.db import models
from django.contrib.auth.models import User


class CreatedUpdatedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Talk(CreatedUpdatedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    speaker = models.ForeignKey('Speaker')
    meetup = models.ForeignKey('Meetup')
    slides = models.URLField()


class Meetup(CreatedUpdatedModel):
    title = models.CharField(max_length=255)
    when = models.DateTimeField()
    venue = models.ForeignKey('Venue')


class Venue(CreatedUpdatedModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Speaker(CreatedUpdatedModel):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=255)
    bio = models.TextField()
    url = models.URLField()
