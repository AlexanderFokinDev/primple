# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#--------------------------------------------------------------------
# Authenticate forms
class MyRegistrationForm(UserCreationForm):
	"""MyRegistrationForm - class for register a new user"""

	email = forms.EmailField(required=True)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'autofocus', 'required':'required'}))
	
	def save(self, commit=True):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		if commit:
			user.save()




#--------------------------------------------------------------------