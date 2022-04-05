from django.db import models

# Create your models here.
class Profile(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    profile_photo = models.CharField(max_length=30)
    bio = models.CharField(max_length=30)
    
class Image(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    image = models.CharField(max_length=30)
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.BooleanField()
    comments = models.CharField(max_length=30) 