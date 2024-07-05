import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
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
