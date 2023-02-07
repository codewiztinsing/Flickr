from django import forms
from django.contrib.auth.forms import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class RegistertionForm(forms.ModelForm):
	password = forms.CharField(label  = "Password",widget = forms.PasswordInput)
	password2 = forms.CharField(label = "confrim password",widget = forms.PasswordInput)

	def clean_password(self):
		cd = self.cleaned_data

		if cd[PasswordInput] != [password2]:
			raise forms.ValidationError("password mismatch")
		return cd['password']

	class Meta:
		model = User
		fields = ('username','first_name','email',)