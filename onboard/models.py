from __future__ import unicode_literals
from django.db import models

class District(models.Model):
    district_name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.district_name

class Student(models.Model):
    district = models.ForeignKey(District)
    activated = models.BooleanField(default=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    student_id = models.CharField(max_length=250)

    def __unicode__(self):
        full_name = self.first_name + " " + self.last_name
        return full_name
