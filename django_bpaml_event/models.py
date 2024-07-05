from django.db import models
from django.contrib.auth.models import AbstractUser


class Event(models.Model):
    code = models.CharField(max_length=20)
    date = models.DateTimeField("date of event")
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=4000)

    def __str__(self):
        return self.title


class User(AbstractUser):
    # add extra field and relationship to admin user
    meetup_name = models.CharField(max_length=200, null=True)
    events = models.ManyToManyField('Event', related_name='attendees', blank=True)

    def __str__(self):
        return f"{self.email}<{self.first_name} {self.last_name}>"
