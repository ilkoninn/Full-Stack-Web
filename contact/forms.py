from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

        fields = ['name', 'email', 'subject', 'desc']

        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control mb-3',
                'placeholder':'Username',
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control mb-3',
                'placeholder':'Email',
            }),
            'subject':forms.TextInput(attrs={
                'class':'form-control mb-3',
                'placeholder':'Subject',
            }),
            'desc':forms.Textarea(attrs={
                'class':'form-control mb-3',
                'placeholder':'Description',
            })
        }