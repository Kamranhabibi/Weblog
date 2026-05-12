from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))


    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get("username"),password=self.cleaned_data.get("password"))
        if user is not None:
            return self.cleaned_data.get("password")
        raise ValidationError("Username or Password is not exist")


class User_Edit_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
