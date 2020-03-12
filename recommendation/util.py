# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/11 3:26 下午
"""
import os
import re
import jieba
import pandas as pd
from mysite import settings


def segment(doc: str):
    """
    中文分词
    :param doc:
    :return:
    """
    # 如果是空值，进行置空处理
    if doc != doc:
        doc = ""

    # stopwords_file = "./data/cn_stopwords.txt"
    stopwords_file = os.path.join(settings.DATA_DIR, "cn_stopwords.txt")

    # 停用词
    stop_words = pd.read_csv(stopwords_file, index_col=False, quoting=3, names=['stopword'], sep="\n", encoding='utf-8')
    stop_words = list(stop_words.stopword)

    reg_html = re.compile(r'<[^>]+>', re.S)
    doc = reg_html.sub('', doc)
    doc = re.sub('[０-９]', '', doc)
    doc = re.sub('\s', '', doc)
    word_list = list(jieba.cut(doc))
    out_str = ''

    for word in word_list:
        if word not in stop_words:
            out_str += word
            out_str += ' '
    segments = out_str.split(sep=" ")

    return segments
