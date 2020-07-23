from django import forms
from IPLteam.models import team

class teamForm(forms.ModelForm):
    class Meta:
        model = team
        fields = '__all__'
