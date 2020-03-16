# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/16 4:36 下午
"""
from django.http import HttpResponse
from .service.userService import add_user


def add_user_controller(request):
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
