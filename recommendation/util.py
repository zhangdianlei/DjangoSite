# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/11 3:26 下午
"""
import os
import re
import jieba
import gensim
import numpy as np
import pandas as pd
from mysite import settings
from collections import Iterable


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


def train_model(file_name: str, model_name: str):
    """
    训练模型数据
    :param model_name:
    :param file_name:
    :return:
    """
    train_file_name = os.path.join(settings.DATA_DIR, file_name)
    model_file_name = os.path.join(settings.MODEL_DIR, model_name)

    train_file = open(train_file_name, "r", encoding="utf-8")
    train_lines = train_file.readlines()

    data = []
    doc_labels = []
    for line in train_lines:
        line_array = line.split("\t")
        movie_title = line_array[1]
        storyline_seg = segment(line_array[16])
        data.append(' '.join(storyline_seg))
        doc_labels.append(' '.join(movie_title))

    print("数据量：", len(data))
    # 训练 Doc2Vec，并保存模型：
    sentences = LabeledLineSentence(data, doc_labels)
    # an empty model
    model = gensim.models.Doc2Vec(vector_size=50, window=10, min_count=5, workers=4, alpha=0.025, min_alpha=0.025,
                                  epochs=10)
    model.build_vocab(sentences)
    print("开始训练...")
    model.train(sentences, total_examples=model.corpus_count, epochs=12)

    model.save(model_file_name)
    print("model saved")
    return "训练结束！"


class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
        self.labels_list = labels_list
        self.doc_list = doc_list

    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
            try:
                yield gensim.models.doc2vec.LabeledSentence(words=doc.split(), tags=[self.labels_list[idx]])
            except:
                print(doc)


def similarity(a_vect, b_vect):
    """计算两个向量余弦值
    Arguments:
        a_vect {[type]} -- a 向量
        b_vect {[type]} -- b 向量

    Returns:
        [type] -- [description]
    """

    dot_val = 0.0
    a_norm = 0.0
    b_norm = 0.0
    cos = None
    for a, b in zip(a_vect, b_vect):
        dot_val += a * b
        a_norm += a ** 2
        b_norm += b ** 2
    if a_norm == 0.0 or b_norm == 0.0:
        cos = -1
    else:
        cos = dot_val / ((a_norm * b_norm) ** 0.5)

    return cos


def sent2vec(model, words):
    """文本转换成向量
    Arguments:
        model {[type]} -- Doc2Vec 模型
        words {[type]} -- 分词后的文本

    Returns:
        [type] -- 向量数组
    """
    vect_list = []
    for w in words:
        try:
            vect_list.append(model.wv[w])
        except:
            continue
    vect_list = np.array(vect_list)
    vect = vect_list.sum(axis=0)
    return vect / np.sqrt((vect ** 2).sum())


def load_model(model_name: str):
    """
    加载模型
    :param model_name:
    :return:
    """
    model_file = os.path.join(settings.MODEL_DIR, model_name)
    print("model loading...")
    model = gensim.models.Doc2Vec.load(model_file)
    print("model load success")
    return model


def calculate_similarity(doc: str):
    """
    计算与输入文本最相似的 doc
    """
    # 加载模型
    model_name = "model_all.model"
    model = load_model(model_name)

    # 目标文档
    dov_seg = segment(doc)

    movie_name = "movie_80000.txt"
    movie_file = os.path.join(settings.MOVIE_SPLIT_DIR, movie_name)

    # 读取需要计算相似度的电影
    current_movie = open(movie_file, "r", encoding="utf-8")
    lines = current_movie.readlines()
    result = {}
    flag = 0
    for line in lines:

        if flag % 100 == 0:
            print("idx", flag)
            flag = flag + 1
        flag = flag + 1

        line_array = line.split("\t")
        title = line_array[1]
        storyline = line_array[16]
        if storyline != storyline:
            continue

        storyline_seg = segment(storyline)

        current_vec = sent2vec(model, dov_seg)
        compare_vec = sent2vec(model, storyline_seg)
        if isinstance(compare_vec, Iterable):
            cos = similarity(current_vec, compare_vec)
            result[title] = cos

    result = sorted(result.items(), key=lambda item: item[1], reverse=True)

    flag = 0
    for index, value in enumerate(result):
        print("title is: ", index, " similarity is:", value)
        flag = flag + 1
        if flag > 10:
            break

    print("相似度计算完成，返回处理结果")
    return result[:10]
