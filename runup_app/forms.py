from django import forms
from django.core.validators import validate_image_file_extension, ValidationError

class UploadImgForm(forms.Form):
    photo = forms.ImageField(required=False)
    album = forms.ImageField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        photo = cleaned_data.get('photo')
        album = cleaned_data.get('album')

        print(photo == None, album == None)

        if (photo == None) != (album == None):
            if photo is None :
                validate_image_file_extension(album)
            else :
                validate_image_file_extension(photo)
        else :
            raise ValidationError("too many images uploaded")
