from django.shortcuts import render
from django.http import HttpResponse
from .util import segment


def index(request):
    return HttpResponse("Hello World1")


def segment_test(request):
    if request.POST:
        print('segment_test')
        doc = request.POST.get("doc", "")
        result = segment(doc)

        return HttpResponse(result)
    else:
        return HttpResponse('请求方法不是post')
