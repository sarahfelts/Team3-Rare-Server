from django.db import models

class Subscription(models.Model):
    follower_id = models.ForeignKey('RareUser', on_delete=models.CASCADE, related_name='follower_subscriptions')
    author_id = models.ForeignKey('RareUser', on_delete=models.CASCADE, related_name='author_subscriptions')
    created_on = models.DateField()
    ended_on = models.DateField()