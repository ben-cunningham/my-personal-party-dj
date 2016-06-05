from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from twilio.twiml import Response


# Handles SMS being recieved
@csrf_exempt
@require_http_methods(["POST"])
def sms_receive(request):
	body = request.POST.get('Body', '')
	

# Handles SMS return code
# @TODO: return spotify return code whether a 
# Request worked or not
@csrf_exempt
@require_http_methods(["GET"])
def sms_write(request):
	r = Response()
	r.message(body)
	return HttpResponse(r.toxml(), content_type='text/xml')
