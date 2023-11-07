from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    ##email=forms.EmailField(required=True,label='Email',error_messages={'exists':'This Already Exists'})
    username = forms.CharField(
        label=("Enter username"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter username'})
    )
    first_name = forms.CharField(
        label=("Enter username"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter username'})
    )
    last_name = forms.CharField(
        label=("Enter username"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter username'})
    )
    email = forms.CharField(
        label=("Enter email-ID"),
        widget=forms.EmailInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter email-ID'})
    )
    password1 = forms.CharField(
        label=("Enter password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter password'})
    )
    password2 = forms.CharField(
        label=("Enter confirm password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter confirm password'})
    )
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
        
class MyLogForm(AuthenticationForm):
    username = forms.CharField(
        label=("Enter username"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter username'})
    )
    password = forms.CharField(
        label=("Enter password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter password'})
    )
    
    
'''
        def __init__(self,*args,**kwargs):
            super(UserCreateForm,self).__init__(*args,**kwargs)
            self.fields['username'].widget.attrs['placeholder']='Username'
            self.fields['email'].widget.attrs['placeholder']='Email'
            self.fields['password'].widget.attrs['placeholder']='Password'
            self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
            
            ''''''
        def save(self,commit=True):
            user=super(UserCreateForm,self).save(commit=False)
            user.email=self.cleaned_data['email']
            if commit:
                user.save()
            return user
        def clean_email(self):
            if User.object.filter(email=self.cleaned_data['email']).exists():
                raise forms.ValidationError(self.fields['email'].error_message['exists'])
            return self.cleaned_data['email']'''