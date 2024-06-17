from django.db import models
from .rare_user import RareUser
from .post import Post

class Comment(models.Model):
    author = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_on = models.DateField()
    
    objects = models.Manager()