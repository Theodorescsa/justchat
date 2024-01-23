from django import forms
from django.contrib.auth.models import User
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)
    
    def clean_password2(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password2 = self.cleaned_data['password2']
        if password2 and password == password2:
            return password2
        raise forms.ValidationError('Mat Khau khong khop hoac khong hop le')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username đã tồn tại')
    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password = self.cleaned_data['password'],
        )
