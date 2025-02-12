from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, EmailValidator

class CreateUserForm(UserCreationForm):
    username = models.CharField(max_length="15",validators=[MinLengthValidator(3)])
    email = models.EmailField(validators=[EmailValidator()])
    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(1)])
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(1)])
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

