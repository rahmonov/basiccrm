from django import forms

from clients.models import Client


class ClientForm(forms.ModelForm):
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


# class ClientForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     birthdate = forms.DateTimeField()
#     phone_number = forms.CharField()
#     address = forms.CharField()
#     gender = forms.ChoiceField(choices=Client.CHOICES)
