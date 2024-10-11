from django import forms
from .models import UserFavouriteArticle

class AddFavouritForm(forms.ModelForm):
	class Meta:
		model = UserFavouriteArticle
		fields = ["article"]

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(AddFavouritForm, self).__init__(*args, **kwargs)
		if user:
			self.user = user
