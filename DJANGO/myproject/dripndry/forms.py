from django import forms
from dripndry.models import dripndry
from dripndry.models import order
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = dripndry
		fields = ('username','password','email','mobile')

class orderform(forms.ModelForm):
	class Meta():
		model = order
		fields = ('pickup_day','slot','immediate_delivery','cloth','quantity','treatment')
class adminform(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = dripndry
		fields = ('username','password','email','mobile')

	

