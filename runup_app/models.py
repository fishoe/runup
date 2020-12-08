from django.db import models
from django.contrib.auth.models import AbstractUser as user_parent
from django.conf import settings

# Create your models here.

class Users(user_parent):
    class GenderCtg(models.IntegerChoices):
        COMMON = 0
        WOMAN = 1
        MAN = 2
    Gender = models.IntegerField(choices=GenderCtg.choices)
    Birth = models.DateField()
    Contact = models.CharField(max_length=25)
    Name = models.CharField(max_length=20)

    class Meta(user_parent.Meta):
        swappable = 'AUTH_USER_MODEL'

class Brands(models.Model):
    Name_kr = models.CharField(max_length=50, unique=True)
    Name_en = models.CharField(max_length=50, unique=True)
    Description = models.TextField(null=True)
    Link = models.URLField()

class MainCategories(models.Model):
    class GenderCtg(models.IntegerChoices):
        WOMAN = 1
        MAN = 2
        COMMON = 3
        NONE = 4
    
    Name_kr = models.CharField(max_length=50)
    Name_en = models.CharField(max_length=50,unique=True) 
    Gender = models.IntegerField(choices=GenderCtg.choices)

class SubCategories(models.Model):
    Name_kr = models.CharField(max_length=50)
    Name_en = models.CharField(max_length=50)
    Main = models.ForeignKey(MainCategories, on_delete= models.CASCADE, related_name='sub_ctgs')

    class GenderCtg(models.IntegerChoices):
        WOMAN = 1
        MAN = 2
        COMMON = 3
        NONE = 4

    Gender = models.IntegerField(choices=GenderCtg.choices)

class Products(models.Model):
    class GenderCtg(models.IntegerChoices):
        COMMON = 0
        WOMAN = 1
        MAN = 2

    Brand = models.ForeignKey(Brands,related_name="Products", on_delete = models.DO_NOTHING)
    Category = models.ForeignKey(SubCategories,related_name='Products', on_delete = models.DO_NOTHING)
    Name = models.CharField(max_length=150)
    Img_url = models.URLField()
    Url = models.URLField()
    Gender = models.IntegerField(choices=GenderCtg.choices)
    Origin_price = models.IntegerField()
    Discount_rate = models.FloatField(null=True)
    Retail_price = models.IntegerField(null=True)
    View_count = models.IntegerField()
    #class color(models.IntegerChoices):
        #pass #컬러 대응표
    #Color = models.IntegerField() #미사용

class Product_Likes(models.Model):
    User = models.ForeignKey(Users,related_name='Like_list', on_delete = models.DO_NOTHING)
    Product = models.ForeignKey(Products,related_name='Like_users', on_delete = models.DO_NOTHING) #prod_obj.Like_users

class Reviews(models.Model):
    User = models.ForeignKey(Users, related_name='Reviews', on_delete = models.DO_NOTHING)
    Product = models.ForeignKey(Products, related_name='Product', on_delete = models.CASCADE )
    Context = models.TextField()
    Rate = models.IntegerField()
    Date = models.DateField()

def rv_dir_path(instance,filename):
    print(instance)
    return f'review_/{filename}'

class Review_imgs(models.Model):
    Review = models.ForeignKey(Users, related_name='Imgs', on_delete = models.DO_NOTHING)
    ImageFile = models.ImageField(upload_to = rv_dir_path)

class Similarities(models.Model):
    Target_prod = models.ForeignKey(Products, related_name='Target_prod',on_delete=models.CASCADE)
    Sim_prod = models.ForeignKey(Products, related_name='Sim_prod',on_delete=models.CASCADE)
    Sim_val = models.FloatField()

class Review_rates(models.Model):
    User = models.ForeignKey(Users, related_name='rated_revies', on_delete = models.DO_NOTHING)
    Review = models.ForeignKey(Reviews, related_name='Rates', on_delete = models.DO_NOTHING)
    Up_down = models.BooleanField()

def rec_dir_path(instance, filename):
    return f'rec/{filename}'

class Recommend_result(models.Model):
    User = models.ForeignKey(Users, related_name='recommends', on_delete = models.DO_NOTHING)
    Result = models.TextField()
    Img = models.ImageField(upload_to = rec_dir_path)
    Date = models.DateField()

class Main_banner(models.Model):
    Start = models.DateField()
    End = models.DateField()
    Img = models.ImageField(upload_to='main_banner/')
    Link = models.URLField()
    Name = models.CharField(max_length=150)

class Img_test(models.Model):
    Products = models.ForeignKey(Products, related_name='Prod',on_delete=models.DO_NOTHING)
    Img = models.ImageField(upload_to='test')