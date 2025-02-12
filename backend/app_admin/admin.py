from django.contrib import admin
from .models import Batdongsan,Profile
# Register your models here.
class BatDongSan_Admin(admin.ModelAdmin):
    list_display  = ("name" ,"category", "year" , "startDate" , "active", "information","local_TT","price","area","author","profile_picture")
    
class Proifle_Admin(admin.ModelAdmin):
    list_display = ("bio" , "birthday" ,"local","phoneNumber")

admin.site.register(Batdongsan, BatDongSan_Admin)
admin.site.register(Profile,Proifle_Admin)
