from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Date(models.Model):
    title = CharField(max_length=400)
    contents = CharField(max_length=1000)
    height = IntegerField()
    weight = IntegerField()
    MBTI = CharField(max_length=100)
    hobby = CharField(max_length=300)
    gender = CharField(max_length=20)
    age = IntegerField()
    user_id = IntegerField()


class Campus_Date(models.Model):
    title = CharField(max_length=400)
    contents = CharField(max_length=1000)
    major = CharField(max_length=100)
    count = IntegerField()
    month = IntegerField()
    day = IntegerField()
    hour = IntegerField()
    major = CharField(max_length=100)
    gender = CharField(max_length=20)
    user_id = IntegerField()

class Comment_Date(models.Model):
  post = models.ForeignKey(Date, on_delete=models.CASCADE, null=True)
  contents = models.CharField(max_length=1000)
  user_id = IntegerField()

class Comment_campus(models.Model):
  post = models.ForeignKey(Campus_Date, on_delete=models.CASCADE, null=True)
  contents = models.CharField(max_length=1000)
  major = models.CharField(max_length=1000)
  user_id = IntegerField()