from django.contrib import admin
from .models import Batdongsan,Profile,Blog
# Register your models here.
class BatDongSan_Admin(admin.ModelAdmin):
    list_display  = ("name" ,"category", "year" , "startDate" , "active", "information","local_TT","price","area","author","profile_picture")
    
class Proifle_Admin(admin.ModelAdmin):
    list_display = ("bio" , "birthday" ,"local","phoneNumber")
    
class Blog_Admin(admin.ModelAdmin):
    list_display = ("title","author","information","dayUpBlog")

admin.site.register(Batdongsan, BatDongSan_Admin)
admin.site.register(Profile,Proifle_Admin)
admin.site.register(Blog,Blog_Admin)