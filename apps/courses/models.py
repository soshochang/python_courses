from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
  name = models.CharField(max_length=38)
  description = models.CharField(max_length= 250)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return "id: " + str(self.id) + ", name: " + self.name