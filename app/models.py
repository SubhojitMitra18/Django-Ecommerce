from django.db import models

# Create your models here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime



class Category(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name
 

class Sub_Category(models.Model):
    name=models.CharField(max_length=150)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    sub_category=models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='ecommerce/pimg')
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
class Order(models.Model):
    image=models.ImageField(upload_to='ecommerce/order/image')
    product=models.CharField(max_length=1000,default='')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=5)
    price=models.IntegerField()
    address=models.TextField()
    phone=models.CharField(max_length=10)
    pincode=models.CharField(max_length=10)
    total=models.CharField(max_length=100,default='')
    date=models.DateField(default=datetime.datetime.today)
    def __str__(self):
        return self.product
    
class Contact_us(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return self.name

    
    






    '''
class UserCreateForm(UserCreationForm):
    email=forms.EmailField(required=True,label='Email',error_messages={'exists':'This Already Exists'})
    
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        
        def __init__(self,*args,**kwargs):
            super(UserCreateForm,self).__init__(*args,**kwargs)
            self.fields['username'].widget.attrs['placeholder']='Username'
            self.fields['email'].widget.attrs['placeholder']='Email'
            self.fields['password'].widget.attrs['placeholder']='Password'
            self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
            
            
        def save(self,commit=True):
            user=super(UserCreateForm,self).save(commit=False)
            user.email=self.cleaned_data['email']
            if commit:
                user.save()
            return user
        def clean_email(self):
            if User.object.filter(email=self.cleaned_data['email']).exists():
                raise forms.ValidationError(self.fields['email'].error_message['exists'])
            return self.cleaned_data['email']
        '''
    
    
