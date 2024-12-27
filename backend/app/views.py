from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TinhThanh
def Index(request):
    return render(request,'index.html')

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
