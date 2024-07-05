from django.urls import path
from django_bpaml_event.views import index_page

urlpatterns = [
  path('', index_page, name='index'),
]
