from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import loader
from .models import TinhThanh
def Index(request):
    return render(request,'index.html')

def adminweb(request):
    template = loader.get_template('adminweb.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def dangki(request):
    template = loader.get_template('dangki.html')
    return HttpResponse(template.render())
def dangnhap(request):
    template = loader.get_template('dangnhap.html')
    return HttpResponse(template.render())

def Blog(request):
    template = loader.get_template('Blog.html')
    return HttpResponse(template.render())

def DangBanBatDongSan(request):
    template = loader.get_template('dangbanbatdongsan.html')
    return HttpResponse(template.render())

def TuyenDung(request):
    template = loader.get_template('tuyendung.html')
    return HttpResponse(template.render())

def TinhThanh(request):
    return HttpResponse("")

def TTDuAn(request):
    return HttpResponse("")
# Create your views here.


    