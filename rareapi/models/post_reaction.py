from django.db import models
from .rare_user import RareUser
from .post import Post
from .reaction import Reaction

class PostReaction(models.Model):
    rare_user_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction_id = models.ForeignKey(Reaction, on_delete=models.CASCADE)