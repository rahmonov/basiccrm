from django import forms
from clients.models import Client
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CustomDateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'business_owner',
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
            'birthdate': CustomDateTimeInput(),
            'phone_number': PhoneNumberPrefixWidget(initial="UZ")
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
