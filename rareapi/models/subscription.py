from django.db import models
from .rare_user import RareUser

class Subscription(models.Model):
    follower_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    author_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    created_on = models.DateField()
    ended_on = models.DateField()