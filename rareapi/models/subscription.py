from django.db import models
from .rare_user import RareUser

class Subscription(models.Model):
    follower_id = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='followed_subscriptions')
    author_id = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='authored_subscriptions')
    created_on = models.DateField()
    ended_on = models.DateField()