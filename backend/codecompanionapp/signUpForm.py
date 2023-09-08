from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	choices = (("SoftwareDeveloper","Software Developer"), 
			("SoftwareDevelopmentManager","Software Development Manager"),
			("HumanResourceManager","Human Resource Manager"))

	email = forms.EmailField(required=True)
	role = forms.ChoiceField(choices=choices)

	class Meta:
		model = User
		fields = ("username", "password1", "password2", "email")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.role = self.cleaned_data['role']
		if commit:
			user.save()
		return user