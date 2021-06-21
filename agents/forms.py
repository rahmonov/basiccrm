from django import forms

from agents.models import Agent

#custome form needs to be used
#froms.Form
# every field need to be created

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
            'business_owner',
        )

