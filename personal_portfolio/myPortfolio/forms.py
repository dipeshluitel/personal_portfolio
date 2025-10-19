from django import forms
from myPortfolio.models import Guest


class GuestForm(forms.ModelForm):
    class Meta():
        model = Guest
        fields = '__all__'