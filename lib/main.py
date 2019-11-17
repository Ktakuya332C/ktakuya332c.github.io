import os
import sys
from typing import List
from lib.view import top as view_top
from lib.view import article as view_article
from lib.errors import BlogError
from lib.entity.article import Article
from lib.io.reader import read_articles


def gen_top(index_path: str,
            root_from_index: str,
            build_dir: str,
            title_str: str,
            desc_str: str,
            footer_str: str,
            articles: List[Article]):
    content: str = view_top.gen(
        root_from_index,
        build_dir,
        title_str,
        desc_str,
        footer_str,
        articles)
    fout = open(index_path, 'w')
    fout.write(content)
    fout.close()


def gen_articles(build_dir: str,
                 root_from_build: str,
                 title_str: str,
                 desc_str: str,
                 footer_str: str,
                 articles: List[Article]):
    for article in articles:
        content: str = view_article.gen(
            root_from_build,
            title_str,
            desc_str,
            footer_str,
            article)
        file_name: str = article.file_name()
        fout_path: str = os.path.join(build_dir, f'{file_name}.html')
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
        fout = open(fout_path, 'w')
        fout.write(content)
        fout.close()


def main(article_dir: str,
         build_dir: str,
         root_from_build: str,
         index_path: str,
         root_from_index: str,
         title_str: str,
         desc_str: str,
         footer_str: str,
         trace_on: bool = False):
    articles: List[Article] = read_articles(article_dir, trace_on=trace_on)
    gen_top(
        index_path,
        root_from_index,
        build_dir,
        title_str,
        desc_str,
        footer_str,
        articles)
    gen_articles(
        build_dir,
        root_from_build,
        title_str,
        desc_str,
        footer_str,
        articles)
