from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
# Create your forms here.


USER_CHOICES= [
    ('Student', 'Student'),
    ('Professor', 'Professor'),
    ]

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	user_type = forms.CharField(label='What type of user are you?', widget=forms.Select(choices=USER_CHOICES))


	class Meta:
		model = User
		fields = ("username", "email", "user_type", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.userType = self.cleaned_data['user_type']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

