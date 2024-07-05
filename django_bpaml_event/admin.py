from django.contrib import admin
from django_bpaml_event.forms import EventAdminForm
from django_bpaml_event.models import Event, User

admin.site.register(User)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
