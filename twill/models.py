from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Number(models.Model):
	phone = models.CharField(max_length=12)

	def get_free():
		raise NotImplementedError