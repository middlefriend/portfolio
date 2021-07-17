from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


'''
class Profile(models.Model):
    #user = models.OneToOneField(User,on_delete=models.CASCADE,db_column='username',related_name='Profile_user')
    user = models.ForeignKey(User,on_delete=models.CASCADE, db_column='username',related_name='Profile_user')
    nickname = models.CharField(max_length=30)
    email = models.EmailField(max_length=128, verbose_name='사용자이메일')
    skin_type = models.PositiveIntegerField(verbose_name=r'피부타입 (지성,건성,민감성 맞으면 1 아니면 0)')
    joined_at = models.DateTimeField(auto_now_add=True)
'''
class Category(models.Model):
    tag_name = models.CharField(max_length=30)

class Cosmetic(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,db_column='tag_name',related_name='Cosmetic_category')
    price = models.PositiveIntegerField()
    maker = models.CharField(max_length=30) 
    capacity = models.PositiveSmallIntegerField()
    rank = models.PositiveSmallIntegerField()
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    award = models.CharField(max_length=200,null=True)
    launch_at = models.DateField()

class Ingredient(models.Model):
    product_id = models.OneToOneField(Cosmetic,on_delete=models.CASCADE,related_name='Ingredient_productid')
    #화장품성분 별 피부타입관계
    oily_skin = models.CharField(max_length=30)
    dry_skin = models.CharField(max_length=30)
    sensitivet_skin = models.CharField(max_length=30)
    #미백,자외선차단,주름개선
    Whitening = models.BooleanField(default=False)
    UV = models.BooleanField(default=False)
    Wrinkle  = models.BooleanField(default=False)
    #화장품 성분 목록들 너무 많아 3개만 넣었음
    purified_water = models.BooleanField(default=False)
    colorant = models.BooleanField(default=False)
    paraben = models.BooleanField(default=False)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Comment_auth')
    product_id = models.OneToOneField(Cosmetic,on_delete=models.CASCADE,related_name='Comment_productid')
    skin_type = models.CharField(max_length=10,verbose_name=r'피부타입 (지성,건성,민감성)')
    strengths = models.TextField()
    weaknesses = models.TextField()
    image_url= models.SlugField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
