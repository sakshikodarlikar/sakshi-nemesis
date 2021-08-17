from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserDetail

# create signup form with password confirmation
class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30, label='username')
    email = forms.EmailField(max_length=254, label='email')
    password1 = forms.CharField(max_length=30, label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, label='password confirmation', widget=forms.PasswordInput)
    address = forms.CharField(max_length=100, label='address')

    # custom validation for password
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    # custom validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):  # check if username already exists
            raise ValidationError("Username already exists")

        return username

    # custom validation for email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__exact=email):  # check if email already exists
            raise ValidationError("Email already exists")
        return email

    # custom validation for address
    def clean_address(self):
        address = self.cleaned_data.get('address')
        if address == "":
            raise ValidationError("Address cannot be empty")
        return address


    # add address in model
    def save(self):
        address = self.cleaned_data.get('address')
        user = User.objects.create(username=self.cleaned_data.get('username'),
                                        email=self.cleaned_data.get('email'),
                                    )
        user.set_password(self.cleaned_data.get('password2'))
        user.save()
        user_details = UserDetail.objects.create(user=user, address=address)
        user_details.save()
        return user_details

# user update form
class UserUpdateForm(forms.Form):
    username = forms.CharField(max_length=30, label='username')
    email = forms.EmailField(max_length=254, label='email')
    address = forms.CharField(max_length=100, label='address')
    password1 = forms.CharField(max_length=30, label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, label='password confirmation', widget=forms.PasswordInput)
    # custom validation for password
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    # custom validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')

        return username

    # custom validation for email
    def clean_email(self):
        email = self.cleaned_data.get('email')

        return email

    # custom validation for address
    def clean_address(self):
        address = self.cleaned_data.get('address')
        if address == "":
            raise ValidationError("Address cannot be empty")
        return address
    
    # add address in model
    def save(self, user_id):
        address = self.cleaned_data.get('address')
        user = User.objects.get(id=user_id)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.save()
        user_details = UserDetail.objects.get(user=user)
        user_details.address = address
        user_details.save()
        return user_details
    
    
        

    
    
