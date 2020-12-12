from django.db import models
from django.contrib.auth.models import AbstractUser as user_parent

# Create your models here.

class users(user_parent):
    class genderctg(models.IntegerChoices):
        COMMON = 0
        WOMAN = 1
        MAN = 2
    email = models.EmailField()
    gender = models.IntegerField(choices=genderctg.choices)
    birth = models.DateField()
    contact = models.CharField(max_length=25)
    name = models.CharField(max_length=20)

    EMAIL_FIELD = 'Email'
    REQUIRED_FIELDS = ['Email','Gender','Birth','Contact','Name']
    
    class Meta(user_parent.Meta):
        swappable = 'AUTH_USER_MODEL'