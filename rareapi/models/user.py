from django.db import models

class User(models.Model):
  first_name = models.CharField(max_length=55)
  last_name = models.CharField(max_length=55)
  bio = models.CharField(max_length=100)
  profile_image_url = models.CharField(max_length=200)
  email = models.CharField(max_length=55)
  created_on = models.DateField()
  active = models.BooleanField()
  is_staff = models.BooleanField(default=False)
  uid = models.CharField(max_length=55)