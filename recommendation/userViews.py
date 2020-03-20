# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/16 4:36 下午
"""
import json
from django.http import HttpResponse, JsonResponse
from .service.userService import add_user, select_id
from django.core import serializers


def add_user_controller(request):
    """
    添加用户
    :param request:
    :return:
    """
    if request.POST:
        name = request.POST.get("name", "")
        age = request.POST.get("age", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "")
        remark = request.POST.get("remark", "")
        result = add_user(name, age, phone, address, remark)

        return HttpResponse(result)
    else:
        return HttpResponse('请求方法不是post')
    add_user()


def select_user(request):
    """
    根据id选择用户
    :param request:
    :return:
    """
    if request.POST:
        data = {}
        user = select_id(request.POST.get("id", 1))
        user_result = serializers.serialize("json", user)
        data["data"] = json.loads(user_result)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("不是POST方法")
