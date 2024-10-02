from django import forms

class sample_form(forms.Form):
	text = forms.CharField(label="Text", max_length=20)
