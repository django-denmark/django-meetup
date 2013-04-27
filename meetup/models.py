from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

(NOT_ATTENDING,
 ATTENDING,
 MAYBE_ATTENDING) = range(3)


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

    def __unicode__(self):
        return u'{title} at {when} at {venue}'.format(
            title=self.title,
            when=self.when,
            venue=self.venue,
        )

    def get_absolute_url(self):
        return reverse('meetup:meetup-detail', kwargs={'pk': self.id})

    def get_attending(self):
        return self.rsvp_set.filter(rsvp=ATTENDING)

    def get_not_attending(self):
        return self.rsvp_set.filter(rsvp=NOT_ATTENDING)

    def get_maybe_attending(self):
        return self.rsvp_set.filter(rsvp=MAYBE_ATTENDING)


class Venue(CreatedUpdatedModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Speaker(CreatedUpdatedModel):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    url = models.URLField(null=True)


class Profile(CreatedUpdatedModel):
    user = models.OneToOneField(User)
    bio = models.TextField()
    url = models.URLField()


class RSVP(CreatedUpdatedModel):

    RSVP_CHOICES = (
        (NOT_ATTENDING, _(u'No')),
        (ATTENDING, _(u'Yes')),
    )

    user = models.ForeignKey(User)
    meetup = models.ForeignKey('Meetup')
    rsvp = models.SmallIntegerField(choices=RSVP_CHOICES)

    class Meta:
        unique_together = ('user', 'meetup')

    def __unicode__(self):
        result = _(u'{user} is {{rsvp}} {meetup}').format(
            user=self.user,
            meetup=self.meetup
        )

        if self.rsvp == NOT_ATTENDING:
            result = result.format(rsvp=_(u'not attending'))
        elif self.rsvp == ATTENDING:
            result = result.format(rsvp=_(u'attending'))

        return result
