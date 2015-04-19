from django.conf import settings
from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=30, blank=True, default='')
    description = models.TextField(blank=True, default='')
    location_lon = models.DecimalField(max_digits=8, decimal_places=5)
    location_lat = models.DecimalField(max_digits=8, decimal_places=5)
    created_on = models.DateTimeField(auto_now_add=True)
    started_on = models.DateTimeField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    group_size = models.IntegerField()

    def __unicode__(self):
        return self.title + ' at ' + str(self.started_on)

    def is_closed(self):
        if self.started_on <= timezone.now(): return True
        return False

    def is_full(self):
        if self.follower_set.count() + 1 >= self.group_size: return True
        return False


class Follower(models.Model):
    event = models.ForeignKey(Event)
    follower = models.ForeignKey(settings.AUTH_USER_MODEL)
    followed_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return ' joins '


