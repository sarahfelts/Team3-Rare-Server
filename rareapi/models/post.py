from django.db import models
from .rare_user import RareUser
from .category import Category

class Post(models.Model):
    rare_user = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=200)
    content = models.CharField(max_length=500)

    approved = models.BooleanField()
