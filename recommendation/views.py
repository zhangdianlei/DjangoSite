from django.shortcuts import render
from django.http import HttpResponse
from .util import segment, train_model, calculate_similarity


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
