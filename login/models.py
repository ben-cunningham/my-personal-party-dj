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
	
	spotify_id = models.CharField(max_length=62)
	current_token = models.CharField(max_length=200)
	playlist_id = models.CharField(max_length=100)
	phone = models.OneToOneField(Number)

	def generate_header(self):
		headers = {'Authorization': 'Bearer ' + 
							self.current_token}
		return headers


def create_profile(spotify_id, token, playlists):
	number = get_free_number()

	user_playlists = [p for p in playlists if p['owner']['id'] == spotify_id]
	selected_playlist = user_playlists[0]['id']
	assert len(user_playlists) > 0, "User has no playlists they own"

	
	profile = Profile.objects.create(
			phone=number,
			spotify_id=spotify_id,
			playlist_id=selected_playlist,
			current_token=token,
	)
	profile.save()
	return profile
