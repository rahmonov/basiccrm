from django import forms
from django.utils import timezone
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from clients.models import Client


class ClientForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='UZ')
    )

    class Meta:
        model = Client
        fields = (
            'business_owner',
            'first_name',
            'last_name',
            'email',
            'birthdate',
            'phone_number',
            'address',
            'gender'
        )

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

