# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2020/3/13 10:46 上午
"""
import os
from mysite import settings
from ..models import Movie


def import_movies():
    movie_name = "movies_all.txt"
    movie_file_name = os.path.join(settings.DATA_DIR, movie_name)

    movie_file = open(movie_file_name, "r", encoding="utf-8")
    lines = movie_file.readlines()

    for idx, line in enumerate(lines):
        if idx == 0:
            continue
        if idx % 100 == 0:
            print("idx:", idx)

        line_array = line.split("\t")

        movie_id = line_array[0]
        name = line_array[1]
        alias = line_array[2]
        actors = line_array[3]
        cover = line_array[4]
        directors = line_array[5]
        douban_score = line_array[6]
        douban_votes = line_array[7]
        genres = line_array[8]
        imdb_id = line_array[9]
        languages = line_array[10]
        mins = line_array[11]
        official_sites = line_array[12]
        regions = line_array[13]
        release_date = line_array[14]
        slug = line_array[15]
        storyline = line_array[16]
        tags = line_array[17]
        year = line_array[18]
        actor_ids = line_array[19]
        director_ids = line_array[20]

        movie = Movie(movie_id=movie_id, name=name, alias=alias, actors=actors, cover=cover, director=directors,
                      douban_score=douban_score, double_vote=douban_votes, genres=genres, imdb_id=imdb_id,
                      language=languages, mins=mins, official_site=official_sites, regions=regions,
                      release_date=release_date, slug=slug, storyline=storyline, tags=tags, year=year,
                      actor_ids=actor_ids, director_ids=director_ids)
        movie.save()

