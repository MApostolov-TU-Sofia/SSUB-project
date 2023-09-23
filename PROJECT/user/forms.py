from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_nbr = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_nbr', 'password1', 'password2']

class UserPasswordChangeForm(PasswordChangeForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
