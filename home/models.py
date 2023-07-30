from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Base(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Activitie(Base):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.name




class Categorie(Base):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=80, blank=True, null=True, editable=False)

    def __str__(self) -> str:
        return self.name


# Teacher Section
class Teacher(Base):
    category = models.ForeignKey(Categorie, related_name="teacher", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Page Section
    cover_img = models.ImageField(upload_to='teachers/cover-img')
    twitter = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=30)
    google = models.CharField(max_length=30)
    

    # Single Section
    teacher_activity = models.ManyToManyField(Activitie, related_name="activity")
    desc = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    skype = models.CharField(max_length=30)
    internet = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='teachers/img')

    # Post Functions
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


# Courses Section
class Course(Base):
    category = models.ForeignKey(Categorie, related_name="course", on_delete=models.CASCADE)
    course_teacher = models.ForeignKey(Teacher, related_name="teacher", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    # Page Section
    img = models.ImageField(upload_to='courses')
    short_desc = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    # Single Section
    money = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    timeline = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    duration = models.DecimalField(max_digits=10, decimal_places=0,blank=True, null=True)
    cover_img = models.ImageField(upload_to='courses/cover-img',blank=True, null=True)
    desc = models.TextField()
    requirements = models.TextField()
    how_to_apply = models.TextField()
    fee_and_funding_about = models.TextField()

    # Post Functions
    slug = models.SlugField(max_length=80, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


# Blogs Section
class Blog(Base):
    user = models.ForeignKey(User, related_name="blog", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    # Page Section
    short_desc = models.TextField()
    cover_img = models.ImageField(upload_to='blog/cover-img', blank=True, null=True)

    # Single Section
    desc = models.TextField()
    img = models.ImageField(upload_to='blog/img', blank=True, null=True)

    # Page Functions
    slug = models.SlugField(max_length=80, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


# Events Section
class Event(Base):
    teachers = models.ManyToManyField(Teacher, related_name="event")
    title = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, null=True)

    # Page Section
    cover_img = models.ImageField(upload_to='event/cover-img')
    short_desc = models.TextField()

    # Single Section
    desc = models.TextField()
    money = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    duration = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    img = models.ImageField(upload_to='event/img')

    # Page Functions
    slug = models.SlugField(max_length=80, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


# Notice Section
class Notice(Base):
    time = models.DateTimeField()
    title = models.CharField(max_length=30)

    # Page Section
    short_desc = models.TextField()

    # Single Section
    desc = models.TextField(blank=True, null=True)

    # Post Functions
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


# Research Section
class Research(Base):

    # Page Section
    title = models.ForeignKey(Categorie, related_name="research", on_delete=models.CASCADE)
    desc = models.TextField()
    cover_img = models.ImageField(upload_to='research/cover-img')

    # Single Section

    # Post Functions
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f"Research {self.title}"


# Scholarship Section
class Scholarship(Base):
    category = models.ForeignKey(Categorie, related_name="scholarship", on_delete=models.CASCADE)

    # Page Section
    title = models.CharField(max_length=30)
    desc = models.TextField()
    cover_img = models.ImageField(upload_to='scholarship/cover-img')

    # Single Section

    # Post Functions
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    

# Subscribtion Section
class Subscribe(Base):
    email = models.EmailField(max_length=150, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.email

