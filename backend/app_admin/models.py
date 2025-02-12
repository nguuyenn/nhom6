from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

#change forms register django
    


class Batdongsan(models.Model):
    name = models.CharField(max_length= 150) #ten bat dong san
    category = models.CharField(max_length=10,blank=True)
    year = models.IntegerField(default= 2024) # nam ban bat dong san
    startDate = models.DateField() # Ngày đăng bán  
    active = models.BooleanField(default=True)# Trạng thái của bds
    information = models.TextField("")
    local_TT = models.CharField(max_length= 50,blank = True)
    price = models.CharField(max_length= 20,blank=True)
    area = models.CharField(max_length=99,blank=True)
    author = models.CharField(max_length= 50,blank=True)
    profile_picture = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return f"{self.name}"

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE) # null=True,on_delete=models.CASCADE nếu xóa user thì hồ sơ người dùng cũng tự động xóa
    bio = models.TextField(null=True)
    birthday = models.DateField(null=True)
    local = models.CharField(null=True,max_length= 255 ) # địa chỉ của người dùng 
    phoneNumber = models.CharField(null=True,max_length= 13)
    profile_picture = models.ImageField(null=True,upload_to='photos/')
    def __str__(self):
        return self.user.username
    @receiver(post_save, sender=User)
    
    def create_user_profile(sender, instance, created, **kwargs):
        # Khi User mới được tạo (created = True), tạo Profile rỗng cho user đó
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

