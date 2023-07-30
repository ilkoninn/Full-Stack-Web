from django.urls import path
from home.api.views import *

urlpatterns = [
    path('categories/', categoriesView, name="categories_api"),
    path('categories/<slug:slug>', categoryViewSlug, name="categories_api_slug"),
    
    path('activities/', activitiesView, name="activities_api"),
    path('activities/<slug:slug>', activityViewSlug, name="activities_api_slug"),
    
    path('blogs/', BlogsView.as_view(), name="blogs_api"),
    path('blogs/<slug:slug>', BlogViewSlug.as_view(), name="blogs_api_slug"),
    
    path('teachers/', TeachersView.as_view(), name="teachers_api"),
    path('teachers/<slug:slug>', TeacherViewSlug.as_view(), name="teachers_api_slug"),
    
    path('events/', EventsView.as_view(), name="events_api"),
    path('events/<slug:slug>', EventViewSlug.as_view(), name="events_api_slug"),

    path('courses/', CoursesView.as_view(), name="courses_api"),
    path('courses/<slug:slug>', CourseViewSlug.as_view(), name="courses_api_slug"),

    path('notices/', NoticesView.as_view(), name="notices_api"),
    path('notices/<slug:slug>', NoticeViewSlug.as_view(), name="notices_api_slug"),

    path('researches/', ResearchesView.as_view(), name="researches_api"),
    path('researches/<slug:slug>', ResearchViewSlug.as_view(), name="researches_api_slug"),

    path('scholarships/', ScholarshipsView.as_view(), name="scholarships_api"),
    path('scholarships/<slug:slug>', ScholarshipViewSlug.as_view(), name="scholarships_api_slug"),
]
