# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/13 10:46 上午
"""
import os
from mysite import settings
from ..models import Intelligence
from ..util import str_similarity


def get_total_rate(doc: str, movie_intros, model):
    """
    获取 综合相似度
    :param model:
    :param doc:
    :param movie_intros:
    :return:
    """

    total_cos = sum(str_similarity(doc, item, model) for item in movie_intros)
    return total_cos


def select_intelligence(intelligence_id):
    """
    根据情报 id 查询情报
    :param intelligence_id:
    :return:
    """
    return Intelligence.objects.get(id=intelligence_id)


def select_recent_intelligence(num, type):
    """
    根据类型查询获取最新的情报数据
    :param num:
    :param type:
    :return:
    """
    return Intelligence.objects.filter(intelligence_type=type).order_by('-time')[0:num]

