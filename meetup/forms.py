from django import forms
import models


class MeetupForm(forms.ModelForm):

    class Meta:
        model = models.Meetup


class VenueForm(forms.ModelForm):

    class Meta:
        model = models.Venue
