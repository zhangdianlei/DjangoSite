# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/11 10:29 上午
"""
from django.urls import path
from . import views, userViews, logViews

urlpatterns = [
    # view
    path('', views.index, name='index'),
    path('segment', views.segment_test),
    path('train', views.train),
    path('similarity_test', views.calculate_sim),
    path('import_movies', views.import_movies),

    # 推荐电影
    path('recommend_movie', views.recommend_movie),

    # user view
    path('add_user', userViews.add_user_controller),
    path('select_user', userViews.select_user),

    # log view
    path('add_log', logViews.add_log_controller),
    path('select_log', logViews.select_recentlog_controller),

]
