from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    """
    用户
    """
    age = models.IntegerField()
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    remark = models.CharField(max_length=64)


class Movie(models.Model):
    """
    电影
    """
    intelligence_id = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    alias = models.TextField()
    actors = models.TextField()
    cover = models.TextField()
    director = models.TextField()
    douban_score = models.CharField(max_length=10)
    double_vote = models.CharField(max_length=10)
    genres = models.CharField(max_length=128)
    imdb_id = models.CharField(max_length=128)
    language = models.CharField(max_length=64)
    mins = models.CharField(max_length=64)
    official_site = models.TextField()
    regions = models.CharField(max_length=64)
    release_date = models.CharField(max_length=64)
    slug = models.CharField(max_length=32)
    storyline = models.TextField()
    tags = models.TextField()
    year = models.TextField()
    actor_ids = models.TextField()
    director_ids = models.TextField()


class UserLogs(models.Model):
    """
    用户记录
    """
    user_id = models.CharField(max_length=128)
    intelligence_id = models.CharField(max_length=128)
    intelligence_type = models.CharField(max_length=64, default="动向情报")
    rate = models.CharField(max_length=64, default="1")
    time = models.DateTimeField()


class Intelligence(models.Model):
    """
    情报信息表
    """
    intelligence_id = models.CharField(max_length=128)
    # 情报类型，分为 "动向情报" "情报产品"
    intelligence_type = models.CharField(max_length=64, default="动向情报")
    title = models.TextField()
    content = models.TextField()
    labels = models.TextField()
    time = models.DateTimeField()


class Result(models.Model):
    """
    推荐结果表
    """
    user_id = models.CharField(max_length=128)
    intelligence_id = models.CharField(max_length=128)
    time = models.DateTimeField()
