import requests
from django.conf.models import Number, Profile

def handle_spotify_query(number, query):
	user = Profile.objects.filter(phone=number)
	active_playlist = user.playlist_id
	token = user.generate_header()






