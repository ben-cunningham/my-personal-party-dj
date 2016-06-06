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
	current_token = models.CharField(max_length=200)
	playlist_id = models.CharField(max_length=100)
	phone = models.OneToOneField(Number)

	def generate_header(self):
		headers = {'Authorization': 'Bearer ' + 
							self.current_token}



def create_profile(spotify_id, headers):
	number = get_free_number()

	def get_playlist():
		playlists_response = requests.get('https://api.spotify.com/v1/me/playlists', headers=headers)
		playlists = json.loads(playlists_response.text)
		if len(playlists['items']) > 0:
			return playlists['items']
		return ""
	
	profile = Profile.objects.create(
			phone=number,
			spotify_id=spotify_id,
			playlist_id=get_playlist() 
	)
	profile.save()
	return profile
