from __future__ import unicode_literals
import uuid
from django.db import models
from onboard.models import District, Student

class ResponseTeam(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    position = models.CharField(max_length=250,blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Alert(models.Model):
    alert_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    district = models.ForeignKey(District)
    student = models.ForeignKey(Student)
    alert_created = models.DateTimeField(auto_now_add=True)
    response_team_activated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
      get_latest_by = 'alert_created'
