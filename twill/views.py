from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml import Response

# Create your views here.

@csrf_exempt
def sms(request):
		r = Response()
		twiml = 'Hello from your Django app!'
		r.message(twiml)
		return HttpResponse(r.toxml(), content_type='text/xml')