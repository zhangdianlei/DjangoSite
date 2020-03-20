# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/16 4:40 下午
"""
from ..models import UserMovieLogs


def add_logs(user_id, movie_id, time):
    """
    添加用户观影记录
    :param user_id:
    :param movie_id:
    :param time:
    :return:
    """
    user_movie_log = UserMovieLogs(user_id=user_id, movie_id=movie_id, time=time)
    user_movie_log.save()


def select_logs(user_id, num):
    """
    查询观影log记录
    :param user_id:
    :param num:
    :return:
    """
    result = UserMovieLogs.objects.filter(user_id__exact=user_id).order_by('-time')[0:num]
    return result

