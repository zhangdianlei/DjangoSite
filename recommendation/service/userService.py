# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/16 4:40 下午
"""
from ..models import User


def add_user(name, age, phone, address, remark):
    """
    添加用户
    :param age:
    :param name:
    :param phone:
    :param address:
    :param remark:
    :return:
    """
    user = User(
        name=name,
        age=age,
        phone=phone,
        address=address,
        remark=remark
    )
    user.save()
