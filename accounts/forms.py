from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

Users = get_user_model()

class AccountForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super

    username = forms.CharField(label='id', min_length=5, max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    name = forms.CharField(label='name')
    birth = forms.DateField(label='birth')
    email =  forms.EmailField(label='email')
    gender = forms.CharField(label='gender',widget=forms.RadioSelect)
    contact = forms.CharField(label='contact')
    pass