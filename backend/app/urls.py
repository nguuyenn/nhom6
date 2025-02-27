from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.Home,name ='Home'),
    path('batdongsan/',views.batdongsans,name='batdongsans'),
    path('batdongsan-edit/<int:id>/',views.edit_batdongsan,name='batdongsan-edit'),
    path('batdongsan-new',views.new_batdongsan,name="batdongsan-new"),
    path('batdongsan-delete/<int:id>/', views.delete_batdongsan, name="batdongsan-delete"),
    path('profile/',views.profile,name ="profile"),
    path('profile/profile-edit',views.edit_profile,name="profile-edit"),
    path('login/',views.login_page,name ='login'),
    path('logout/',views.Logout_page ,name='logout'),
    path('register',views.Register,name='register'),
    path('search/',views.search_view,name='search'),
    path('blog',views.blogs,name ="blog"),
    path('blog/<int:blog_id>/', views.detail_blog, name='blog-detail'),
    path('blog-new',views.new_blog,name = 'blog-new'),
    path('tuyendung',views.TuyenDung,name="tuyendung"),
    
]