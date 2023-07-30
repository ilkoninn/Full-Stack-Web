from django import forms
from home.models import *

class SubcribtionForm(forms.ModelForm):

    class Meta:
        model = Subscribe
        fields = ['email']
        
        widgets = {
            'email': forms.EmailInput(attrs={
                'class':'form-control border-0',
                'placeholder': 'Enter Your Email'
            })
        }
