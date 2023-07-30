from django.contrib import admin
from home.models import *
# Register your models here.

# Admin Course Section
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = [
        'title', 'desc', 'short_desc', 'requirements', 
        'how_to_apply', 'fee_and_funding_about','img', 
        'cover_img', 'date', 'duration', 'timeline', 'money',
        'category', 'course_teacher', 'slug'  
    ]
    search_fields = ['category__name', 'title', 'money', 'course_teacher']
    list_filter = ['category', 'course_teacher']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = [
        'first_name', 'last_name', 'email', 'phone', 
        'desc', 'biography', 'cover_img','img', 'category',
        'facebook', 'twitter', 'linkedin', 'google', 
        'skype', 'internet', 'teacher_activity', 'location', 
        'slug'
    ]
    search_fields = ['category__name', 'faculty', 'title']
    list_filter = ['category',]

admin.site.register([
    Categorie,
    Activitie,
    Scholarship,
    Blog, 
    Event, 
    Notice,
    Research,
    Subscribe,
])

