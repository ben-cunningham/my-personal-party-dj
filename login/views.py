from django.shortcuts import redirect
from django.http import HttpResponse

import datetime
import base64
import requests

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
	headers = {
		'Authorization': 'Basic ' +base64.b64encode(auth_header)
	}
	print headers
	print data
	r = requests.post('https://accounts.spotify.com/api/token', data=data, headers=headers)
	print r.text
	return HttpResponse()

def main(request):
	print request
	return HttpResponse()

