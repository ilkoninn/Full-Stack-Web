from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from home.models import *


@receiver(pre_save, sender = Blog)
def BlogSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Activitie)
def ActivitySignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
    return instance

@receiver(pre_save, sender = Categorie)
def CategorySignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
    return instance

@receiver(pre_save, sender = Teacher)
def TeacherSignal(sender, instance, **kwargs):
    instance.slug = slugify(f'{instance.first_name} {instance.last_name}')
    return instance

@receiver(pre_save, sender = Course)
def CourseSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Event)
def EventSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Notice)
def NoticeSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Research)
def ResearchSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Scholarship)
def ScholarshipSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Subscribe)
def SubscribeSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.email)
    return instance
