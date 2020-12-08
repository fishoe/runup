from django import forms

class UploadImgForm(forms.Form):
    photo = forms.ImageField()