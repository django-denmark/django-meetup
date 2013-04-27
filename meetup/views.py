from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required

from .models import Meetup
from .forms import MeetupForm


class MeetupList(ListView):
    model = Meetup
    template_name = 'meetup/meetup_list.html'
    context_object_name = 'meetups'


class MeetupDetail(DetailView):
    model = Meetup
    template_name = 'meetup/meetup_detail.html'
    context_object_name = 'meetup'


class MeetupCreate(CreateView):
    model = Meetup
    form = MeetupForm

    @login_required
    def dispatch(self, request, *args, **kwargs):
        return super(MeetupCreate, self).dispatch(request, *args, **kwargs)
