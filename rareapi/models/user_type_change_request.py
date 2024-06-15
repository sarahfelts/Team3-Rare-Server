from django.db import models
from .rare_user import RareUser

class UserTypeChangeRequest(models.Model):
    action = models.CharField(max_length=55)
    admin_one_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    admin_two_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    modified_user_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)