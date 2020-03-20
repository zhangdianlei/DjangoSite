# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/20 9:14 上午
"""
import json
from django.http import HttpResponse, JsonResponse
from .service.logService import add_logs, select_logs
from django.core import serializers
from datetime import datetime


def add_log_controller(request):
    """
    添加用户观影记录
    :param request:
    :return:
    """
    if request.method == 'POST':
        logs = json.loads(request.body)
        for log in logs:
            user_id = log["user_id"]
            movie_id = log["movie_id"]
            time = datetime.strptime(log["time"], '%Y-%m-%d %H:%M:%S')
            add_logs(user_id, movie_id, time)

        return HttpResponse('添加成功')
    else:
        return HttpResponse('请求方法不是post')


def select_recentlog_controller(request):
    """
    查询最近记录
    :param request:
    :return:
    """
    if request.POST:
        user_id = request.POST.get("user_id")
        num = int(request.POST.get("num"))
        result = select_logs(user_id, num)

        data = {}
        user_result = serializers.serialize("json", result)
        data["data"] = json.loads(user_result)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse('请求方法不是post')
