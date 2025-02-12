from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from app_admin.models import Batdongsan,Profile
from django.core.validators import RegexValidator
from django.utils import timezone

class BatDongSan_Form(forms.ModelForm):
    name = forms.CharField(max_length=150, required=False)
    category = forms.CharField(max_length=10, required=False)
    year = forms.IntegerField(required=True, initial=2024)
    startDate = forms.DateField(required=True)
    active = forms.BooleanField(required=False, initial=True)
    information = forms.CharField(widget=forms.Textarea, required=False)
    local_TT = forms.CharField(max_length=50, required=False)
    price = forms.CharField(max_length=20, required=False)
    area = forms.CharField(max_length=99, required=False)
    author = forms.CharField(max_length=50, required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Batdongsan
        fields = ['name', 'category', 'year', 'startDate', 'active', 'information', 'local_TT', 'price', 'area', 'author', 'profile_picture']

class UpdateUserForm(UserChangeForm):
    password = None
    username = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            return self.instance.username
        return username
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial values for empty fields
        instance = kwargs.get('instance')
        if instance:
            self.fields['first_name'].initial = instance.first_name or "Không có thông tin"
            self.fields['last_name'].initial = instance.last_name or "Không có thông tin"
            self.fields['email'].initial = instance.email or "Không có thông tin"

class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea)
    birthday = forms.DateField(required=False)
    local = forms.CharField(required=False)
    phoneNumber = forms.CharField(required=False)
    profile_picture = forms.ImageField(required=False)
    
    class Meta:
        model = Profile
        fields = ('bio', 'birthday', 'local', 'phoneNumber', 'profile_picture')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial values for empty fields
        instance = kwargs.get('instance')
        if instance:
            self.fields['bio'].initial = instance.bio or "Không có thông tin"
            self.fields['local'].initial = instance.local or "Không có thông tin"
            self.fields['phoneNumber'].initial = instance.phoneNumber or "Không có thông tin"
            if instance.birthday:
                self.fields['birthday'].initial = instance.birthday
            else:
                self.fields['birthday'].initial = None
        
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')