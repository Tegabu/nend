from email.mime import image
from email.policy import default
import unicodedata
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
import uuid


User = get_user_model()

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile_images', default='person.png')
    phone = models.IntegerField(default='0')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField(max_length=_MAX_LENGTH, blank=True)
    post_date = models.DateTimeField(default=datetime.now)
    num_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class likepost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class product(models.Model):
    name = models.CharField(max_length=100)
    prodesc = models.TextField(max_length=_MAX_LENGTH, blank=False)
    pic = models.ImageField(upload_to='post_images')
    price = models.DecimalField(max_digits=6, decimal_places=2)


class host(models.Model):
    name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)
    info = models.TextField(max_length=_MAX_LENGTH, blank=False)
    charge = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    img = models.ImageField(upload_to='post_images')
