<<<<<<< HEAD
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    
=======


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
>>>>>>> 6d95b7a92f801cf9d992d401174c5bfea691f7dd
