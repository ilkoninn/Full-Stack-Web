from django.urls import path
from home.views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('research/', research, name="research"),
    path('scholarship/', scholarship, name="scholarship"),
    

    path('courses/', courses, name="courses"),
    path('courses/<slug:slug>/', courses, name="courses_slug"),
    path('course-single/<slug:slug>/', course_single , name="course_single"),
    
    path('events/', events, name="events"),
    path('event-single/<slug:slug>', event_single, name="event_single"),
    
    path('blogs/', blogs, name="blogs"),
    path('blog/<slug:slug>', blog_single, name="blog_single"),
    
    path('notices/', notices, name="notices"),
    path('notice-single/<slug:slug>', notice_single, name="notice_single"),
    
    path('teachers/', teachers, name="teachers"),
    path('teachers/<slug:slug>', teachers, name="teachers_slug"),
    path('teacher-single/<slug:slug>', teacher_single, name='teacher_single'),

    path('subscribe/', subscribe, name="subscribe"),
]


