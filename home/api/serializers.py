from gettext import translation
from django.contrib.auth import get_user_model
from home.models import *
from rest_framework import serializers

User = get_user_model()


class SerialCategory(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    slug = serializers.SlugField(read_only = True)

    def create(self, validated_data):
        data = Categorie.objects.create(**validated_data)
        return data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
class SerialActivity(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()

    def create(self, validated_data):
        data = Activitie.objects.create(**validated_data)
        return data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class SerialUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SerialBlog(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date',]
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

class SerialTeacher(serializers.ModelSerializer):
    teacher_activity = serializers.PrimaryKeyRelatedField(queryset = Activitie.objects.all(), many = True)
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
    
    def create(self, validated_data):
        teachers_data = validated_data.pop('teacher_activity', [])
        obj = super().create(validated_data)

        if teachers_data:
            obj.teacher_activity.set(teachers_data)
        
        return obj
    
class SerialEvent(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), many=True)
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
    
    def create(self, validated_data):
        teachers_data = validated_data.pop('teachers', [])
        obj = super().create(validated_data)

        if teachers_data:
            obj.teachers.set(teachers_data)
        
        return obj

class SerialCourse(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
    
    def create(self, validated_data):
        return Course.objects.create(**validated_data)

class SerialNotice(serializers.ModelSerializer):
    
    class Meta:
        model = Notice
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
    
    def create(self, validated_data):
        return Notice.objects.create(**validated_data)

class SerialResearch(serializers.ModelSerializer):

    class Meta:
        model = Research
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
    
    def create(self, validated_data):
        return Research.objects.create(**validated_data)

class SerialScholarship(serializers.ModelSerializer):

    class Meta:
        model = Scholarship
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']

    def create(self, validated_data):
        return Scholarship.objects.create(**validated_data)

