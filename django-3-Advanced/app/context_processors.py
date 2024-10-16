from django.contrib.auth.forms import AuthenticationForm

def login_form(request):
    # Only add the form if the user is not authenticated
    if not request.user.is_authenticated:
        return {'login_form': AuthenticationForm()}
    return {}
