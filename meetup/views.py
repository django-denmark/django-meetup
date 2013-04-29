from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

import models
import forms


class MeetupList(generic.TemplateView):
    template_name = 'meetup/meetup_list.html'
    #context_object_name = 'meetups'
    #model = models.Meetup

    def get_context_data(self, *args, **kwargs):
        context = super(MeetupList, self).get_context_data(*args, **kwargs)

        meetups = models.Meetup.objects.extra(
            select={
                "num_attending": """
                SELECT count(*) from meetup_rsvp r
                WHERE r.rsvp=2 and r.meetup_id = meetup_meetup.id
                """
            }
        ).select_related('venue')

        #meetups = models.Meetup.objects.all()

        context.update({
            'meetups': meetups,
        })

        return context


class MeetupDetail(generic.DetailView):
    model = models.Meetup
    template_name = 'meetup/meetup_detail.html'
    context_object_name = 'meetup'

    def get_context_data(self, *args, **kwargs):
        context = super(MeetupDetail, self).get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated():
            try:
                user_rsvp = self.request.user.rsvp_set.get(
                    meetup=self.get_object()
                ).rsvp
            except models.RSVP.DoesNotExist:
                user_rsvp = None

            context.update({
                'user_rsvp': user_rsvp,
            })

        rsvps = self.get_object().rsvp_set.order_by('rsvp').iterator()

        context.update({
            'rsvps': rsvps,
        })

        return context

    def post(self, *args, **kwargs):
        rsvp_value = self.request.POST.get('rsvp', None)

        if rsvp_value:

            try:
                rsvp = models.RSVP.objects.get(
                    meetup=self.get_object(),
                    user=self.request.user,
                )
            except models.RSVP.DoesNotExist:
                rsvp = models.RSVP(
                    user=self.request.user,
                    meetup=self.get_object(),
                )

            rsvp.rsvp = rsvp_value

            rsvp.save()

            messages.success(self.request, 'Your RSVP has been recorded.')

        else:
            messages.warning(self.request, 'No RSVP valueNo RSVP value!!')

        return redirect(
            reverse(
                'meetup:meetup-detail',
                kwargs={'pk': self.get_object().id}
            )
        )


class MeetupCreate(generic.CreateView):
    model = models.Meetup
    form = forms.MeetupForm
    template_name = 'meetup/meetup_form.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MeetupCreate, self).dispatch(request, *args, **kwargs)


class VenueCreate(generic.CreateView):
    model = models.Venue
    form = forms.VenueForm
    template_name = 'meetup/venue_form.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VenueCreate, self).dispatch(request, *args, **kwargs)


class VenueDetail(generic.DetailView):
    model = models.Venue
    template_name = 'meetup/venue_detail.html'
    context_object_name = 'venue'


class VenueList(generic.ListView):
    model = models.Venue
    template_name = 'meetup/venue_list.html'
    context_object_name = 'venues'
