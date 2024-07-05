from django.urls import path
from django_bpaml_event.views import index_page, event_page, attend

urlpatterns = [
  path('', index_page, name='index'),
  path('event/<str:code>/', event_page, name='event'),
  path('event/attend/<str:code>/<str:rsvp>/', attend, name='attend'),
]
