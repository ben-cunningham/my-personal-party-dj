import requests
from twill.models import Number
from login.models import Profile
import json

def handle_spotify_request(number, query):
	user = Profile.objects.get(phone=number)
	user_id = user.spotify_id
	active_playlist = user.playlist_id
	headers = user.generate_header()
	query = query.replace(' ', '+')


	return_values = requests.get(
			'https://api.spotify.com/v1/search?type=track&q=' + query,
			 headers=headers)

	req_song_id = json.loads(
				return_values.text)['tracks']['items'][0]['id']

	add_to_playlist_string = 'https://api.spotify.com/v1/users/%s/playlists/%s/tracks' % \
							(user_id, active_playlist)

	# https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks
	playlist_add = requests.get(
					add_to_playlist_string,
					headers=headers)

	print playlist_add


def test():
	return handle_spotify_request(
			'+16042568089',
			'kanye west power')
