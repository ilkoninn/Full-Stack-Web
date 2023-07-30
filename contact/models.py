from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=40)
    desc = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name
