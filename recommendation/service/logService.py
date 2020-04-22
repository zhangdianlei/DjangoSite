# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/16 4:40 下午
"""
from ..models import UserLogs


def add_logs(user_id, intelligence_id, time):
    """
    添加记录
    :param user_id:
    :param intelligence_id:
    :param time:
    :return:
    """
    user_log = UserLogs(user_id=user_id, intelligence_id=intelligence_id, time=time)
    user_log.save()


def select_logs(user_id, num):
    """
    查询log记录
    :param user_id:
    :param type:
    :param num:
    :return:
    """
    result = UserLogs.objects.filter(user_id__exact=user_id).order_by('-time')[0:num]
    return result

