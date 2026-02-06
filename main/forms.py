from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactMessage


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class EditProfileForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(max_length=100, required=False)
	last_name = forms.CharField(max_length=100, required=False)

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')


class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactMessage
		fields = ('name', 'email', 'subject', 'message')
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
			'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
			'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
			'message': forms.Textarea(attrs={'placeholder': 'Your message...', 'class': 'materialize-textarea'}),
		}
