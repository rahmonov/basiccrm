from django import forms
from django.utils import timezone

from clients.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'first_name',
            'last_name',
            'email',
            'birthdate',
            'phone_number',
            'address',
            'gender',
            'profile_picture'
        )
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_birthdate(self):
        cleaned_data = self.clean()
        birthdate = cleaned_data['birthdate']

        if birthdate >= timezone.now():
            raise forms.ValidationError("Birthdate cannot be in future")

        return birthdate

    def clean_email(self):
        cleaned_data = self.clean()
        email = cleaned_data['email']

        _, domain = email.split('@')

        if domain != 'gmail.com':
            raise forms.ValidationError('Invalid domain. Only gmail.com is allowed!')

        return email
