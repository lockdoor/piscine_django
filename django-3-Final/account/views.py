from django.contrib.auth.views import LoginView
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.middleware.csrf import get_token

# Create your views here.

class ConnectLoginView(LoginView):
	def form_invalid(self, form):
		return JsonResponse({
			'success': False,
			'errors': form.error_messages
		}, safe=False)

	def form_valid(self, form):
		user = form.get_user()
		login(self.request, user)
		token = get_token(self.request)
		return JsonResponse({
			'success': True,
			'message': 'Successfully connected',
			'csrf_token': token,
			'username': user.username
		}, safe=False)

class CustomLogoutView(View):
	def post(self, request, *args, **kwargs):
		# Log the user out
		logout(request)

		# Get the new CSRF token after logout
		csrf_token = get_token(request)

		# Return JSON response with the new CSRF token
		return JsonResponse({
			'success': True,
			'message': 'Successfully logged out',
			'csrf_token': csrf_token
		})
