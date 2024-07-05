import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from allauth.account.decorators import login_required
from django_bpaml_event.models import Event


def index_page(request):
    """Find all events with an event date later than yesterday"""
    yesterday = timezone.now() - datetime.timedelta(days=1)
    list_future_events = Event.objects.filter(date__gte=yesterday).order_by("code")
    context = {'list_events': list_future_events}
    return render(request, 'django_bpaml_event/index.html', context)


def event_page(request, code):
    e = get_object_or_404(Event, code=code)
    context = {'event': e}
    return render(request, 'django_bpaml_event/event.html', context)


@login_required()
def attend(request, code, rsvp):
    """Set registration status for logged-in user as not attending
    code: event code
    rsvp: yes or no or true or false"""
    user = request.user
    e = get_object_or_404(Event, code=code)
    # Add to event on y, yes, Y, Yes, t, True, true
    if rsvp is None or len(rsvp) < 1:
        pass  # do nothing
    if rsvp.lower()[:1] in 'yt':
        user.events.add(e)
    elif rsvp.lower()[:1] in 'nf':
        user.events.remove(e)
    url_next = request.GET.get('next')
    if url_next is None:
        context = {'event': e}
        return render(request, 'django_bpaml_event/event.html', context)
    else:
        return HttpResponseRedirect(url_next)