from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    birth = models.DateField()
    gender = models.CharField(max_length=5)
    # def str(self):
    #     return self.user.id
