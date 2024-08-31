# forms.py

from django import forms
from django.contrib.auth.models import User

class CheckoutForm(forms.Form):
    pays = forms.CharField(max_length=100, required=True)
    ville = forms.CharField(max_length=100, required=True)
    numero_de_telephone = forms.CharField(max_length=15, required=True)
    adresse = forms.CharField(max_length=255, required=True)
    code_postale = forms.CharField(max_length=20, required=False)

class CreateAccountForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    numero_de_telephone = forms.CharField(label='Numéro de téléphone', max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'numero_de_telephone']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return password2
