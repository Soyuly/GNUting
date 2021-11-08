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


class Campus_Date(models.Model):
    title = CharField(max_length=400)
    contents = CharField(max_length=1000)
    major = CharField(max_length=100)
    count = IntegerField()
    month = IntegerField()
    day = IntegerField()
    hour = IntegerField()
