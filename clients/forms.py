from django import forms
from clients.models import Client


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

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'




# class ClientForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     birthdate = forms.DateTimeField()
#     phone_number = forms.CharField()
#     address = forms.CharField()
#     gender = forms.ChoiceField(choices=Client.CHOICES)
