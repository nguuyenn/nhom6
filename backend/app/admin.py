from django.contrib import admin
<<<<<<< HEAD
=======

# Register your models here.
from django.contrib import admin

from .models import TinhThanh, TTDuAn, BatDongSan


admin.site.register(BatDongSan)
class TinhThanhAdmin(admin.ModelAdmin):
     list_display =["ten_tinh_thanh"]
class TTDUAnAdmin(admin.ModelAdmin):
    list_display = ("tieu_de","gia_ban","dia_chi","ngay_ban")

admin.site.register(TinhThanh,TinhThanhAdmin)
admin.site.register(TTDuAn,TTDUAnAdmin)
>>>>>>> 6d95b7a92f801cf9d992d401174c5bfea691f7dd
