from django.shortcuts import redirect
from django.http import HttpResponse
import datetime

def login(request):
	url = 'https://accounts.spotify.com/authorize?client_id=f3ee976a08f14c70bcb93f8bc020e019&redirect_uri=https%3A%2F%2Flimitless-chamber-26833.herokuapp.com%2Fcallback%2F&response_type=code'
	print url
	return redirect(url) 

def app(request):
	print request
	return HttpResponse()
