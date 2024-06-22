from django.db import models

class RareUser(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    bio = models.CharField(max_length=100)
    profile_image_url = models.CharField(max_length=200)
    email = models.EmailField(max_length=55)
    created_on = models.DateField()
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True)
    uid = models.TextField(max_length=55)
    
    objects = models.Manager()
