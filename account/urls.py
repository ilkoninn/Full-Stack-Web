from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import *
from django.contrib.auth import views as auth_views
from account.views import MyPasswordResetView

urlpatterns = [
    path('login/', mylogin, name='login'),
    path('logout/', mylogout, name='logout'),
    path('register/', myregister, name='register'),
    path('profile/', profile, name='profile'),
    path('create-blog/', create_blog, name="create_blog"),
    path('edit-blog/<slug:slug>', edit_blog, name="edit_blog"),
    path('reset-password/', reset_pass, name="reset_pass"),
    path('change-password/', change_pass, name="change_pass"),

    path('password_reset/', MyPasswordResetView.as_view(), name='forget_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

