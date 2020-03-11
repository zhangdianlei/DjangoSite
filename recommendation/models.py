from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=64)
    user_phone = models.IntegerField()


class Item(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=64)
