from django.shortcuts import render, redirect

from home.models import *
from home.api.serializers import *
from home.api.permissions import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status


@api_view(['GET', 'POST'])
def categoriesView(request):
    if request.method == "GET":
        categories = Categorie.objects.all()
        serial = SerialCategory(categories, many = True)
        return Response(serial.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        data = SerialCategory(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data = data.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def categoryViewSlug(request, slug):
    try:
        category = Categorie.objects.get(slug = slug)
    except:
        return Response(data={
                'error':'Category not found'
            }, status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serial = SerialCategory(category)
        return Response(serial.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serial = SerialCategory(category, request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status.HTTP_200_OK)

    elif request.method == 'DELETE':
        category.delete()
        return Response(data={'delete':'Success'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def activitiesView(request):
    if request.method == "GET":
        categories = Activitie.objects.all()
        serial = SerialActivity(categories, many = True)
        return Response(serial.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        data = SerialActivity(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data = data.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def activityViewSlug(request, slug):
    try:
        activity = Activitie.objects.get(slug = slug)
    except:
        return Response(data={
                'error':'Activity not found'
            }, status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serial = SerialActivity(activity)
        return Response(serial.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serial = SerialActivity(activity, request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status.HTTP_200_OK)

    elif request.method == 'DELETE':
        activity.delete()
        return Response(data={'delete':'Success'}, status=status.HTTP_200_OK)


class BlogsView(ListCreateAPIView):
    serializer_class = SerialBlog
    queryset = Blog.objects.all()

class BlogViewSlug(RetrieveUpdateDestroyAPIView):
    serializer_class = SerialBlog
    queryset = Blog.objects.all()
    lookup_field = "slug"

    # permission_classes = [IsOwner]

    # def perform_update(self, serializer):
    #     serializer.save(modified_by=self.request.user)
        

class TeachersView(ListCreateAPIView):
    serializer_class = SerialTeacher
    queryset = Teacher.objects.all()

class TeacherViewSlug(RetrieveUpdateDestroyAPIView):
    serializer_class = SerialTeacher
    queryset = Teacher.objects.all()
    lookup_field = "slug"

    # permission_classes = [IsOwner]

    # def perform_update(self, serializer):
    #     serializer.save(modified_by=self.request.user)

class EventsView(ListCreateAPIView):
    serializer_class = SerialEvent
    queryset = Event.objects.all()


class EventViewSlug(RetrieveUpdateDestroyAPIView):
    serializer_class = SerialEvent
    queryset = Event.objects.all()
    lookup_field = "slug"

    # permission_classes = [IsOwner]

    # def perform_update(self, serializer):
    #     serializer.save(modified_by=self.request.user)

class CoursesView(ListCreateAPIView):
    serializer_class = SerialCourse
    queryset = Course.objects.all()

class CourseViewSlug(RetrieveUpdateDestroyAPIView):
    serializer_class = SerialCourse
    queryset = Course.objects.all()
    lookup_field = "slug"

    # permission_classes = [IsOwner]

    # def perform_update(self, serializer):
    #     serializer.save(modified_by=self.request.user)

class NoticesView(ListCreateAPIView):
    serializer_class = SerialNotice
    queryset = Notice.objects.all()

class NoticeViewSlug(RetrieveUpdateDestroyAPIView):
    serializer_class = SerialNotice
    queryset = Notice.objects.all()
    lookup_field = "slug"

    # permission_classes = [IsOwner]

    # def perform_update(self, serializer):
    #     serializer.save(modified_by=self.request.user)

class ResearchesView(ListCreateAPIView):
    serializer_class = SerialResearch
    queryset = Research.objects.all()

class ResearchViewSlug(RetrieveUpdateDestroyAPIView):
    serializer_class = SerialResearch
    queryset = Research.objects.all()
    lookup_field = "slug"

    # permission_classes = [IsOwner]

    # def perform_update(self, serializer):
    #     serializer.save(modified_by=self.request.user)

class ScholarshipsView(ListCreateAPIView):
    serializer_class = SerialScholarship
    queryset = Scholarship.objects.all()

class ScholarshipViewSlug(RetrieveUpdateDestroyAPIView):
    serializer_class = SerialScholarship
    queryset = Scholarship.objects.all()
    lookup_field = "slug"

    # permission_classes = [IsOwner]

    # def perform_update(self, serializer):
    #     serializer.save(modified_by=self.request.user)



#--------------------------------------------------------------------------------------------------#

# class ActivitiesView(APIView):
#     def get(self, request, *args, **kwargs):
#         activities = Activitie.objects.all()
#         serial = SerialActivity(activities, many = True, context={'request':request})
#         return Response(data = serial.data, status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):
#         activity_data = SerialActivity(data = request.data)
#         if activity_data.is_valid():
#             activity_data.save()
#             return Response(data = activity_data.data, status=status.HTTP_201_CREATED)
#         return Response(data = activity_data.errors, status=status.HTTP_400_BAD_REQUEST)

# class BlogsView(APIView):
#     def get(self, request, *args, **kwargs):
#         blogs = Blog.objects.all()
#         serial = SerialBlog(blogs, many = True, context = {'request':request})
#         return Response(data = serial.data, status=status.HTTP_200_OK)

#     def post(self, request, *args, **kwargs):
#         blog_data = SerialBlog(data = request.data)
#         if blog_data.is_valid():
#             blog_data.save(
#                 img = request.data.get('img'),
#                 cover_img = request.data.get('cover_img'),
#             )
#             return Response(data = blog_data.data, status=status.HTTP_201_CREATED)
#         return Response(data = blog_data.errors, status=status.HTTP_400_BAD_REQUEST)

#--------------------------------------------------------------------------------------------------#