from django.shortcuts import redirect, render
from django.http import HttpResponse

import datetime
import base64
import requests
import json

def get_playlists(headers):
	playlists = requests.get('https://api.spotify.com/v1/me/playlists', headers=headers)
	return playlists


def login(request):
	url = 'https://accounts.spotify.com/authorize?client_id=f3ee976a08f14c70bcb93f8bc020e019&redirect_uri=https%3A%2F%2Ff0f02446.ngrok.io%2Fcallback%2F&response_type=code'
	return redirect(url) 

def app(request):
	code = request.GET.get('code')
	data = {
		'code': code,
		'redirect_uri': 'https://f0f02446.ngrok.io/callback/',
		'grant_type': 'authorization_code',
	}

	auth_header = 'f3ee976a08f14c70bcb93f8bc020e019' +':' +'84103952ba0f48f88080090c9b1962a2'
	encoded = base64.b64encode(auth_header)
	headers = {
		'Authorization': 'Basic ' +encoded
	}
	r = requests.post('https://accounts.spotify.com/api/token', data=data, headers=headers)

	json_data = json.loads(r.text)
	headers = {
		'Authorization': 'Bearer ' + json_data['access_token']
	}
	playlists = get_playlists(headers)

	return render(request, 'playlists.html', {'playlists': playlists})

def main(request):
	return HttpResponse()

