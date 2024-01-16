from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField
from django_resized import ResizedImageField
from django.db import models


# Create your models here.
class User(AbstractUser):
    image = ResizedImageField(size=[90, 90], crop=['middle', 'center'], upload_to='users/images',
                              default='users/default.jpg')


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField()
    projects = models.IntegerField(default=0)
    image = ImageField(default='employees/default.jpg',upload_to='employees/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


