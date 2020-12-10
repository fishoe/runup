from django import forms
from .models import Users
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
        model = Users
        fields = ['username','password1','password2','name','birth','email','gender','contact']

    def save(self):
        user = super().save(commit=False)
        user.Name = self.cleaned_data['name']
        user.Birth = self.cleaned_data['birth']
        user.Email = self.cleaned_data['email']
        user.Contact = self.cleaned_data['contact']
        user.Gender = 1 if self.cleaned_data['gender'] == 'w' else 2
        return user

    