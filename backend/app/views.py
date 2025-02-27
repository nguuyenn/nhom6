import os
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from app_admin.models import Batdongsan,Blog
from .forms import BatDongSan_Form,UpdateUserForm, UpdateProfileForm,BlogForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from datetime import date
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
def Home(request):
    return render(request,'home.html')

def batdongsans(request):
    batdongsans = Batdongsan.objects.all()
    template = loader.get_template('app_home/batdongsan/batdongsan.html')
    context ={
        'batdongsan' : batdongsans,
    }
    return HttpResponse(template.render(context,request))

@login_required
def edit_batdongsan(request, id):
     # Kiem tra nguoi dung da dang nhap chua 
    if not request.user.is_authenticated:
        messages.warning(request, 'Bạn cần phải đăng nhập để chỉnh sửa bất động sản.')
        return render(request, 'app_home/batdongsan/batdongsan-edit.html', {
            'message': 'Bạn cần phải đăng nhập để chỉnh sửa bất động sản.'
        })
    batdongsan = get_object_or_404(Batdongsan, id=id) 
    old_image = batdongsan.profile_picture  # Lưu đường dẫn ảnh cũ
    
    if request.method == 'POST':
        form = BatDongSan_Form(request.POST, request.FILES, instance=batdongsan)
        if form.is_valid():
            # Kiểm tra xem có upload ảnh mới không
            if 'profile_picture' in request.FILES:
                # Nếu có ảnh cũ, xóa ảnh cũ
                if old_image:
                    import os
                    if os.path.isfile(old_image.path):
                        os.remove(old_image.path)
                        
            # Lưu form với ảnh mới
            form.save()
            return redirect('batdongsans')
        else:
            print(form.errors)
    else:
        form = BatDongSan_Form(instance=batdongsan)
    
    context = {
        'form': form,
        'batdongsan': batdongsan,
    }
    return render(request, 'app_home/batdongsan/batdongsan-edit.html', context)
        
@login_required
def delete_batdongsan(request,id):
    batdongsan = Batdongsan.objects.get(id = id)
    if request.method == "POST":
        batdongsan.delete()
        return redirect('/batdongsan')
    context ={
        'batdongsan':batdongsan
    }
    return render(request, 'app_home/batdongsan/batdongsan-delete.html', context)


def new_batdongsan(request):
        # Nếu người dùng gửi form qua POST
    if request.method == 'POST':
        form = BatDongSan_Form(request.POST, request.FILES)
        
        if form.is_valid():
            # Nếu form hợp lệ, tạo và lưu đối tượng Batdongsan
            form.save()
            return redirect('batdongsans')  # Điều hướng đến trang chi tiết bất động sản vừa đăng
            
        else:
            messages.error(request, 'Error updating profile')
    
    else:
        # Nếu yêu cầu là GET, hiển thị form đăng bán
        form = BatDongSan_Form()

    return render(request, 'app_home/batdongsan/batdongsan-new.html', {'form': form})
    


def profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'app_home/user/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            # xu ly user form
            user = user_form.save(commit=False)
            
            if not user.username:
                user.username = request.user.username
            
            # reset cac truong neu no ko co thong tin
            for field in ['first_name', 'last_name', 'email']:
                if getattr(user, field) == "Không có thông tin":
                    setattr(user, field, None)
            
            user.save()
            
            # xu ly form hinh anh
            profile = profile_form.save(commit=False)
            profile.user = user
            
            # Reset fields to None if they contain "Không có thông tin"
            for field in [ 'bio', 'local', 'phoneNumber']:
                if getattr(profile, field) == "Không có thông tin":
                    setattr(profile, field, None)
            
            # xu ly hinh anh
            if 'profile_picture' in request.FILES:
                if profile.profile_picture:
                    try:
                        old_image_path = profile.profile_picture.path
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    except:
                        pass
                profile.profile_picture = request.FILES['profile_picture']
            
            profile.save()
            
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'app_home/user/profile-edit.html', context)




#Bỏ qua kiểm tra token CSRF cho các yêu cầu gửi đến hàm
@csrf_exempt
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)
        
        if user is not None:
            login(request,user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('/') 
        else:
            messages.info(request,'User name of password is Incorrect!')
            
    return render(request,'login.html',{})
        

def search_view(request):
    if request.method == 'POST':
        # Lấy các giá trị từ form tìm kiếm
        name_search = request.POST.get('searched', '')
        category_search = request.POST.get('category', '')
        location_search = request.POST.get('location', '')
        
        # Lọc các bds đang active
        properties = Batdongsan.objects.filter(active=True)
        
        # Lọc theo tên
        if name_search:
            properties = properties.filter(name__icontains=name_search)
            
        # Tìm theo category nếu không phải chọn tìm tất cả
        if category_search and category_search != 'all':
            properties = properties.filter(category=category_search)
            
        # Tìm theo địa điểm 
        if location_search:
            properties = properties.filter(local_TT__icontains=location_search)
        
        context = {
            'name_searched': name_search,
            'category_searched': category_search,
            'location_searched': location_search,
            'properties': properties,
        }
        
        return render(request, 'search_results.html', context)

def Logout_page(request):
    logout(request)
    return redirect('/')

def Register(request):
    # Khởi tạo form trống cho GET request
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
            
    context = {
        'form': form,
        'title': 'Register'  # Thêm title để test có thể kiểm tra
    }
    
    return render(request, 'register.html', context)



def blogs(request):
    blog_posts = Blog.objects.all().order_by('-dayUpBlog')
    
    context = {
        'blog_posts': blog_posts,
    }
    
    return render(request, 'app_home/blog/blog.html', context)
    
    
def detail_blog(request,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'app_home/blog/blog-detail.html', context)


def new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.dayUpBlog = date.today()
            blog.save()
            return redirect('blog')
    else:
        form = BlogForm()
    
    return render(request, 'app_home/blog/blog-new.html', {'form': form})

def TuyenDung(request):
    template = loader.get_template('tuyendung.html')
    return HttpResponse(template.render())

