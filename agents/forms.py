from django import forms

from users.models import BusinessOwner

#custome form needs to be used
#froms.Form
# every field need to be created


class AgentForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    region = forms.CharField(max_length=100)
    business_owner = forms.ModelChoiceField(queryset=BusinessOwner.objects.all())