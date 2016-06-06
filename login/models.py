from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

from twill.models import Number, get_free_number

# Create your models here.

""" 
USR has spotify token
and a phone attributed to them
1:1 relation with django user model
"""


class Profile(models.Model):
	# user = models.OneToOneField(	
	#		User, on_delete = models.CASCADE)
	
	spotify_id = models.CharField(max_length=100)
	playlist_id = models.CharField(max_length=100)
	phone = models.OneToOneField(Number)

def create_profile(spotify_id):
	number = get_free_number()

	def get_playlist():
		pass

	profile = Profile.objects.create(
			phone=number.phone,
			spotify_id=spotify_id,
			playlist_id=playlist_id
	)
	profile.save()
	return profile