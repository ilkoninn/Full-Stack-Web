from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import *
from home.models import Blog
from django.contrib.auth.views import PasswordResetView
# Create your views here.

def mylogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            messages.add_message(request, messages.WARNING, "Username or password incorrect!")

    return render(request=request, template_name='login.html')

def mylogout(request):
    logout(request)
    return redirect(reverse_lazy('login'))

def myregister(request):
    forms = RegisterForm()
    context = {'forms':forms}

    if request.method == "POST":
        data = RegisterForm(request.POST)
        if data.is_valid():
            user = data.save()
            user.set_password(user.password)
            user.save()
            return redirect(reverse_lazy('login'))
        else:
            context = {'forms':forms}
            messages.add_message(request, messages.ERROR, "Entered information is not correct!")

    return render(request=request, template_name='register.html', context=context)

def create_blog(request):
    forms = CreateBlogForm()
    context = {'forms':forms}

    if request.method == "POST":
        data = CreateBlogForm(request.POST, request.FILES)
        if data.is_valid():
            blog = data.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect(reverse_lazy('profile'))
        else:
            context = {'forms':forms}

    return render(request=request, template_name="create_story.html", context=context)

def edit_blog(request, slug):
    forms = CreateBlogForm()
    blog = Blog.objects.get(slug = slug)
    context = {
        'forms':forms,
        'blog_data':blog,
    }
    
    if request.method == "POST":
        data = CreateBlogForm(request.POST or None, instance=blog)
        if data.is_valid():
            data.save()
            return redirect(reverse_lazy('profile'))
    else:
        context = {
            'forms':forms,
            'blog_data':blog,
        }

    return render(request=request, template_name="edit_story.html", context=context)

@login_required
def profile(request):
    context = {
        "blogs_data":Blog.objects.filter(user = request.user)
    }
    return render(request=request, template_name='profile.html', context=context)

def change_pass(request):
    return render(request=request, template_name="change_password.html")

def reset_pass(request):
    return render(request=request, template_name="reset_password.html")

class MyPasswordResetView(PasswordResetView):
    template_name = 'forget_password.html'
