from django import forms
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _

from weatherappauth.models import WeatherAppUser


class RegistrationForm(forms.ModelForm):

	email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=255)), label=("Email address"))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True)), label=("Password"))
	password_repeat = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True)), label=("Repeat Password"))

	def clean_email(self):
		try:
			user = WeatherAppUser.objects.get(email__iexact=self.cleaned_data.get('email'))
		except WeatherAppUser.DoesNotExist:
			return self.cleaned_data['email']
		raise forms.ValidationError(_("The email already exists. Please try another one."))

	def clean(self):
		# Check that the two password entries match
		password = self.cleaned_data.get("password")
		password_repeat = self.cleaned_data.get("password_repeat")
		if password and password_repeat and password != password_repeat:
			raise forms.ValidationError("Passwords don't match")
		return self.cleaned_data

	class Meta:
		model = WeatherAppUser
		fields = ['email']