from django import forms
from django.contrib.auth.models import User 
from home.models import Blog
class RegisterForm(forms.ModelForm):

    confirmPass = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm password',
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Last Name',
            }),
            'username': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Username',
            }),
            'email': forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Password',
            })
        }
    
    def clean(self):
        confirmPass = self.cleaned_data.get('confirmPass')
        password = self.cleaned_data.get('password')

        if confirmPass != password:
            raise forms.ValidationError('Confirm password and password incorrect! ')
        
        
        return super().clean()
    

class CreateBlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = [
            'title','short_desc', 'desc',
            'img', 'cover_img',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Blog Title',
            }),
            'short_desc': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Blog Short Description',
            }),
            'desc': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Blog Description',
            }),
            'img': forms.FileInput(attrs={
                'class':'form-control',
                'placeholder':'Blog Image'
            }),
            'cover_img': forms.FileInput(attrs={
                'class':'form-control',
                'placeholder':'Blog Cover Image',
            })
        }