from django import forms
from .models import Meetup


class MeetupForm(forms.ModelForm):

    class Meta:
        model = Meetup
