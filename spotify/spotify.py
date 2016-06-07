import requests
from twill.models import Number
from login.models import Profile
import json

def handle_spotify_request(number, query):
	number = int(number.split("+")[1])
	try:
		user = Profile.objects.get()
	except StandardError:
		print "no phones left"

	user_id = user.spotify_id
	active_playlist = user.playlist_id
	if active_playlist is None:
		pass
	
	headers = user.generate_header()
	query = query.replace(' ', '+')


	return_values = requests.get(
			'https://api.spotify.com/v1/search?type=track&q=' + query,
			 headers=headers)

	print "Search song query return code: " + str(return_values)
	
	req_song_uri = json.loads(
				return_values.text)['tracks']['items'][0]['uri']

	data = {'uris': [req_song_uri]}
	uri_string = 'uris=' + req_song_uri

	add_to_playlist_string = 'https://api.spotify.com/v1/users/%s/playlists/%s/tracks?%s' % \
							(user_id, active_playlist, uri_string)

	# https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks
	playlist_add = requests.post(
					add_to_playlist_string,
					#data=data,
					headers=headers)
	import pdb;pdb.set_trace()
	print "Playlist add return code: " + str(playlist_add)

	if playlist_add.status_code == 201:
		# Return success text
	else:
		# Return fail text


def test():
	return handle_spotify_request(
			'+16042568089',
			'kanye west power')
