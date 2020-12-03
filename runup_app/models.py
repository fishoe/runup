from django.db import models
from django.contrib.auth.models import AbstractUser as user_parent

# Create your models here.

class Users(user_parent):
    Gender = models.BooleanField()
    Birth = models.DateField()
    Contact = models.TextField()
    Name = models.TextField()

    class Meta(user_parent.Meta):
        swappable = 'AUTH_USER_MODEL'

class Brands(models.Model):
    Name_kr = models.TextField()
    Name_en = models.TextField()
    Description = models.TextField()
    Link = models.URLField()

class Categories(models.Model):
    Name = models.TextField()
    Main = models.TextField()
    Sub = models.TextField()

class Products(models.Model):
    Brand = models.ForeignKey(Brands,related_name="Products", on_delete = models.DO_NOTHING)
    Category = models.ForeignKey(Categories,related_name='Products', on_delete = models.DO_NOTHING)
    Name = models.TextField()
    Img_url = models.URLField()
    Url = models.URLField()
    Origin_price = models.IntegerField()
    Discount_rate = models.FloatField()
    Retail_price = models.IntegerField()
    View_count = models.IntegerField()
    #Color = models.IntegerChoices() #미사용

class Product_Likes(models.Model):
    User = models.ForeignKey(Users,related_name='Like_list', on_delete = models.DO_NOTHING)
    Product = models.ForeignKey(Products,related_name='Like_users', on_delete = models.DO_NOTHING) #prod_obj.Like_users

class Reviews(models.Model):
    User = models.ForeignKey(Users, related_name='Reviews', on_delete = models.DO_NOTHING)
    Product = models.ForeignKey(Products, related_name='Product', on_delete = models.CASCADE )
    Context = models.TextField()
    Rate = models.IntegerField()
    UserImg = models.ImageField()
    Date = models.DateField()

class Similarities(models.Model):
    Target_prod = models.ForeignKey(Products, related_name='Target_prod',on_delete=models.CASCADE)
    Sim_prod = models.ForeignKey(Products, related_name='Sim_prod',on_delete=models.CASCADE)
    Sim_val = models.FloatField()

class Review_rates(models.Model):
    User = models.ForeignKey(Users, related_name='rated_revies', on_delete = models.DO_NOTHING)
    Review = models.ForeignKey(Reviews, related_name='Rates', on_delete = models.DO_NOTHING)
    Up_down = models.BooleanField()

class Recommend_result(models.Model):
    User = models.ForeignKey(Users, related_name='recommends', on_delete = models.DO_NOTHING)
    Result = models.TextField()
    Img = models.ImageField()
    Date = models.DateField()

class Main_banner(models.Model):
    Start = models.DateField()
    End = models.DateField()
    Img = models.ImageField()
    Link = models.URLField()
    Name = models.TextField()
