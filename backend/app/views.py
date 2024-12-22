from django.shortcuts import render
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'Blog.html')

def dangbanbatdongsan(request):
    return render(request, 'dangbanbatdongsan.html')

def tuyendung(request):
    return render(request, 'tuyendung.html')

# Create your views here.
