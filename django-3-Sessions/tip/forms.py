from django import forms
from .models import Tip
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class SignInForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ['username', 'password']

class CreateTip(forms.ModelForm):
	class Meta:
		model = Tip
		fields = ['content']
