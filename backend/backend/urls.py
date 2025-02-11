

from django.contrib import admin
from django.urls import path,include
from app import views   # type: ignore # Replace 'my_app' with the actual name of your application

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('adminweb/', views.adminweb, name='adminweb'),
    path('login/', views.login, name='login'),
    path('dangki/', views.dangki, name='dangki'),
    path('dangnhap/', views.dangnhap, name='dangnhap'),
    path('blog/', views.Blog, name='blog'),
    path('dangbanbatdongsan/', views.DangBanBatDongSan, name='dangbanbatdongsan'),
    path('tuyendung/', views.TuyenDung, name='tuyendung'),
    path('',include('app.urls')),
]
