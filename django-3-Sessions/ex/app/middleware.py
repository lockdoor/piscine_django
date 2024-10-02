import sys
import random
import time
from django.conf import settings

class RandomNameMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if not request.session.get('username') or \
			time.time() - request.session.get('timestamp', 0) > 42:
			request.session['username'] = random.choice(settings.RANDOM_NAME)
			request.session['timestamp'] = time.time()
		response = self.get_response(request)
		return response
