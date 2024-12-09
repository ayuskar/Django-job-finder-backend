from django.db import models
from django.contrib.auth.models import User
#Model for profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    skills = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return self.user.username