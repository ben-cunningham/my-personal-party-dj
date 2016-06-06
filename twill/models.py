from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Number(models.Model):
	phone = models.CharField(max_length=12, primary_key=True)
	active = models.BooleanField(default=False)
	
	def set_number_used(self):
		self.active = True


def get_free_number():
	free_numbers = Number.objects.filter(active=False)
	first_free = free_numbers[0]
	first_free.set_number_used()
	return first_free

