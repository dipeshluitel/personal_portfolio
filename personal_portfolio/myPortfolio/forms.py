from django import forms
from myPortfolio.models import Guest


class GuestForm(forms.ModelForm):
    class Meta():
        model = Guest
        fields = '__all__'
        widgets={
            'firstname': forms.TextInput(attrs={'class':'form-input'}),
            'lastname': forms.TextInput(attrs={'class':'form-input'}),
            'email': forms.TextInput(attrs={'class':'form-input', 'placeholder':'someone@mail.com'}),
            'content': forms.Textarea(attrs={'class':'form-input form-text-input', 'placeholder':'Enter Additional Message if necessary'}),
        }