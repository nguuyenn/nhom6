from django.db import models
<<<<<<< HEAD
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, EmailValidator

class CreateUserForm(UserCreationForm):
    username = models.CharField(max_length="15",validators=[MinLengthValidator(3)])
    email = models.EmailField(validators=[EmailValidator()])
    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(1)])
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(1)])
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

=======
# class Example(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
# Create your models here.
from django.db import models
# Create your models here.
# Model for TinhThanh (Provinces)

class TinhThanh(models.Model):
    ten_tinh_thanh = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ten_tinh_thanh}"


# # Model for DuAn (Projects)
# class DuAn(models.Model):
#     tieu_de = models.CharField(max_length=100)
#     gia_ban = models.BigIntegerField(99999999999) # gia max la 100000000-1 ty
#     dia_chi = models.CharField(max_length=255)
#     mo_ta = models.TextField()
#     ngay_ban = models.DateField()
#     def __str__(self):
#         return self.tieu_de
#Thong tin du an
class TTDuAn(models.Model):
    tieu_de = models.CharField(max_length=100)
    gia_ban = models.CharField(max_length =10) # gia max la 100000000-1 ty
    dia_chi = models.CharField(max_length=255)
    mo_ta = models.TextField()
    ngay_ban = models.DateField()
    #tinh_trang =models.BooleanField()
    def __str__(self):
        return f"{self.tieu_de},{self.ngay_ban}"
class UserMember(models.Model):
    # account = models.CharField(max_length= 30)
    # password = models.CharField(max_length= 30)
    ten = models.CharField(max_length=25)
    gioi_tinh = models.BooleanField()
    so_dien_thoai = models.CharField(max_length= 11)
    
        


# Model for BatDongSan (Real Estate)
class BatDongSan(models.Model):
    LOAI_CHOICES = [
        ('Nhà ở', 'Nhà ở'),
        ('Đất', 'Đất'),
    ]

    # loai = models.CharField(max_length=50, choices=LOAI_CHOICES)
    # dia_chi = models.CharField(max_length=255)
    # gia = models.DecimalField(max_digits=15, decimal_places=2)
    # tinh_thanh = models.ForeignKey(TinhThanh, on_delete=models.CASCADE)
    # du_an = models.ForeignKey(TTDuAn, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.loai} - {self.dia_chi}"
>>>>>>> 6d95b7a92f801cf9d992d401174c5bfea691f7dd
