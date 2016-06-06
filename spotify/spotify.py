import requests
from twill.models import Number
from login.models import Profile

def handle_spotify_request(number, query):
	user = Profile.objects.filter(phone=number)[0]
	active_playlist = user.playlist_id
	headers = user.generate_header()
	query = query.replace(" ", "%20")



	return_values = requests.get('https://api.spotify.com/v1/search?type=track&q=' + query, headers=headers)

	print return_values




def test():
	handle_spotify_request('+16042568089', "kanye west power")
