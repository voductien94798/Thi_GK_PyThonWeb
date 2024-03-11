import re
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2') 
        if password1 != password2:
            raise forms.ValidationError("Mật khẩu không trùng khớp")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản không được chứa kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
class LoginForm(forms.Form):
    username = forms.CharField(label='Tài khoản')
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
