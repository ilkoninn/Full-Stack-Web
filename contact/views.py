from django.shortcuts import render
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib import messages
# Create your views here.


def contact(request):
    forms = ContactForm()
    context = {'forms': forms }
    if request.user.is_authenticated:
        if request.method == "POST":
            data = ContactForm(request.POST)
            if data.is_valid():
                Contact.objects.create(
                    name = data.cleaned_data['name'],
                    email = data.cleaned_data['email'],
                    subject = data.cleaned_data['subject'],
                    desc = data.cleaned_data['desc'],
                )
            else:
                context = {'forms':forms}
    else:
        messages.add_message(request, messages.WARNING, "If you want to contact us, you'd sign in!")

    return render(request=request, template_name='contact.html', context=context)
