from django.db import models
from accounts.models import users

# Create your models here.

class brands(models.Model):
    name_kr = models.CharField(max_length=50, unique=True)
    name_en = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    link = models.URLField()

class maincategories(models.Model):
    class genderctg(models.IntegerChoices):
        WOMAN = 1
        MAN = 2
        COMMON = 3
        NONE = 4
    
    name_kr = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50,unique=True) 
    gender = models.IntegerField(choices=genderctg.choices)

class subcategories(models.Model):
    name_kr = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    main = models.ForeignKey(maincategories, on_delete= models.CASCADE, related_name='sub_ctgs')

    class genderctg(models.IntegerChoices):
        WOMAN = 1
        MAN = 2
        COMMON = 3
        NONE = 4

    gender = models.IntegerField(choices=genderctg.choices)

class products(models.Model):
    class genderctg(models.IntegerChoices):
        COMMON = 0
        WOMAN = 1
        MAN = 2

    brand = models.ForeignKey(brands,related_name="products", on_delete = models.DO_NOTHING)
    category = models.ForeignKey(subcategories,related_name='products', on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=150)
    img_url = models.URLField()
    url = models.URLField()
    gender = models.IntegerField(choices=genderctg.choices)
    origin_price = models.IntegerField()
    discount_rate = models.FloatField(null=True)
    retail_price = models.IntegerField(null=True)
    view_count = models.IntegerField()
    #class color(models.IntegerChoices):
        #pass #컬러 대응표
    #Color = models.IntegerField() #미사용

class product_likes(models.Model):
    user = models.ForeignKey(users,related_name='Like_list', on_delete = models.DO_NOTHING)
    product = models.ForeignKey(products,related_name='Like_users', on_delete = models.DO_NOTHING) #prod_obj.Like_users

class reviews(models.Model):
    user = models.ForeignKey(users, related_name='Reviews', on_delete = models.DO_NOTHING)
    product = models.ForeignKey(products, related_name='Product', on_delete = models.CASCADE )
    context = models.TextField()
    rate = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

def rv_dir_path(instance,filename):
    return f'review_{instance.review}/{filename}'

class review_imgs(models.Model):
    review = models.ForeignKey(reviews, related_name='Imgs', on_delete = models.DO_NOTHING)
    imagefile = models.ImageField(upload_to = rv_dir_path)

class similarities(models.Model):
    target_prod = models.ForeignKey(products, related_name='target_prod',on_delete=models.CASCADE)
    sim_prod = models.ForeignKey(products, related_name='Sim_prod',on_delete=models.CASCADE)
    sim_val = models.FloatField()

class review_rates(models.Model):
    user = models.ForeignKey(users, related_name='rated_revies', on_delete = models.DO_NOTHING)
    review = models.ForeignKey(reviews, related_name='Rates', on_delete = models.DO_NOTHING)
    up_down = models.BooleanField()

def rec_dir_path(instance, filename):
    if instance.user is None:
        return f'rec/anonymous/{filename}'
    else :
        return f'rec/{instance.user.id}/{filename}'

class scatch_result(models.Model):
    user = models.ForeignKey(users,null=True , related_name='Scatch_results', on_delete = models.DO_NOTHING)
    result = models.TextField()
    img = models.ImageField(upload_to = rec_dir_path)
    date = models.DateTimeField(auto_now_add=True)

class main_banner(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    img = models.ImageField(upload_to='main_banner/')
    link = models.URLField()
    name = models.CharField(max_length=150)