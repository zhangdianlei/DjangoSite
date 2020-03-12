# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/11 10:29 上午
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('segment', views.segment_test)
]
