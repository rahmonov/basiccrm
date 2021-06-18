from django import forms
from clients.models import Client
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'agent',
            'first_name',
            'last_name',
            'birthdate',
            'email',
            'phone_number',
            'address',
            'gender',
            'profile_picture'
        )
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': PhoneNumberPrefixWidget(initial="UZ")
        }

