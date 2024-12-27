

from django.contrib import admin
from django.urls import path,include
from app import views   # type: ignore # Replace 'my_app' with the actual name of your application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('blog/', views.Blog, name='blog'),
    path('dangbanbatdongsan/', views.DangBanBatDongSan, name='dangbanbatdongsan'),
    path('tuyendung/', views.TuyenDung, name='tuyendung'),
    path('',include('app.urls')),
]
