from django import forms
from .models import Login,Create_ak,Contact

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['email','password']
        
class Create_akForm(forms.ModelForm):
    class Meta:
        model = Create_ak
        fields = ['name','email','password']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']