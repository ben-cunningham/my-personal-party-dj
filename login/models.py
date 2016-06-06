from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

""" 
USR has spotify token
and a phone attributed to them
1:1 relation with django user model
"""


class Profile(models.Model):
	user = models.OneToOneField(
		User, on_delete = models.CASCADE)

	phone = models.CharField(max_length=12)
	playlist = models.CharField(max_length=100)