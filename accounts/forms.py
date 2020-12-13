from django import forms
from .models import users
from django.contrib.auth.forms import UserCreationForm

class AccountForm(UserCreationForm):
    password1 = forms.CharField(label='password1',widget = forms.PasswordInput)
    password2 = forms.CharField(label='password2',widget = forms.PasswordInput)
    name = forms.CharField(label='name')
    birth = forms.DateField(label='birth', widget=forms.DateInput)
    email =  forms.EmailField(label='email',widget=forms.EmailInput)
    gender = forms.CharField(label='gender',widget=forms.RadioSelect)
    contact = forms.CharField(label='contact')

    class Meta :
        model = users
        fields = ['username','password1','password2','name','birth','email','gender','contact']

    def save(self):
        user = super().save(commit=False)
        user.name = self.cleaned_data['name']
        user.birth = self.cleaned_data['birth']
        user.email = self.cleaned_data['email']
        user.contact = self.cleaned_data['contact']
        user.gender = self.cleaned_data['gender']
        return user

    