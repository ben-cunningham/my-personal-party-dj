from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from twilio.twiml import Response
from spotify.spotify import handle_spotify_request


# Handles SMS being recieved
@csrf_exempt
@require_http_methods(["POST"])
def sms_receive(request):
	twill_number = request.POST.get('To', '')
	spotify_query = request.POST.get('Body', '')

	string = "My number is %s" % (twill_number)
	## GET BODY in form of (request, param, number that was texted)
	## Based off of phone number, retrieve spotify token in database
	## Connect to api based on request
	## Pipe to associated method and execute request with params


	handle_spotify_request(twill_number, spotify_query)
	'''
	r = Response()
	r.message(string)
	return HttpResponse(r.toxml(), content_type='text/xml')
	'''

# Handles SMS return code
# @TODO: return spotify return code whether a 
# Request worked or not
@csrf_exempt
@require_http_methods(["GET"])
def sms_write(request):
	r = Response()
	r.message("Sup")
	return HttpResponse(r.toxml(), content_type='text/xml')
