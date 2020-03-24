from datetime import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .util import segment, train_model, calculate_similarity
from .service.movieService import import_movies as movie2db, select_movies, get_total_rate
from .service.logService import select_logs
from .models import Movie
from .util import load_model
from django.core import serializers


def index(request):
    return HttpResponse("Hello World1")


def segment_test(request):
    """
    分词实验
    :param request:
    :return:
    """
    if request.POST:
        print('segment_test')
        doc = request.POST.get("doc", "")
        result = segment(doc)

        return HttpResponse(result)
    else:
        return HttpResponse('请求方法不是post')


def train(request):
    """
    训练模型
    :param request:
    :return:
    """
    if request.POST:
        print("train_model")
        file_name = request.POST.get("file_name", "")
        model_name = request.POST.get("model_name", "")
        result = train_model(file_name, model_name)

        return HttpResponse(result)
    else:
        return HttpResponse("请求方法不是post")


def calculate_sim(request):
    """
    计算相似度
    :param request:
    :return:
    """
    if request.POST:
        print("start calculate similarity")
        doc = request.POST.get("doc", "")
        result = calculate_similarity(doc)

        return HttpResponse(result)
    else:
        return HttpResponse("请求方法不是post")


def import_movies(request):
    """
    将电影数据引入数据库
    :param request:
    :return:
    """
    print("开始将电影数据引入数据库...")
    movie2db()

    print("导入完成")
    return HttpResponse("导入完成")


def recommend_movie(request):
    """
    传入用户 id 和 movie_id，返回推荐的电影序列结果
    :param request:
    :return:
    """
    if request.method == 'POST':
        params = json.loads(request.body)
        user_id = params["user_id"]
        movies = params["movies"]
        user_movie_logs = select_logs(user_id, 20)
        history_movies = [item.movie_id for item in user_movie_logs]
        print("history_movies", history_movies)

        history_movie_intros = [select_movies(item).storyline for item in history_movies]

        current_movies = [Movie.objects.get(id=item) for item in movies]

        # 加载模型
        model_name = "model_all.model"
        model = load_model(model_name)

        for movie in current_movies:
            cos = get_total_rate(movie.storyline, history_movie_intros, model)
            movie.cos = cos

        print("current_movies", current_movies)
        current_movies.sort(key=lambda x: x.cos, reverse=True)

        data = []
        for item in current_movies:
            temp_data = {
                "id": item.id,
                "cos": item.cos,
                "movie_id": item.movie_id,
                "name": item.name
            }
            data.append(temp_data)

        return HttpResponse(json.dumps(data), content_type="application/json")

    else:
        return HttpResponse('请求方法不是post')
