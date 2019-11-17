import os
import glob
import datetime
from typing import List
from lib.errors import ParseError
from lib.entity.article import Article
from lib.compiler.converter import Converter


def read_article(article_path: str, trace_on: bool = False) -> Article:

    # 記事ファイルを読み込む
    fin = open(article_path, 'r')
    title_str: str = fin.readline()
    title_str = title_str.strip()
    date_str: str = fin.readline()
    date_str = date_str.strip()
    content: str = fin.read()
    content = content.strip()
    fin.close()

    # 日付をdatetime.date型に変換
    try:
        date_time: datetime.datetime = datetime.datetime.strptime(
            date_str, "%Y-%m-%d")
    except ValueError as e:
        raise ParseError(str(e))
    date = date_time.date()

    # 内容をコンパイル
    content = Converter(content, trace_on=trace_on).execute()

    return Article(title_str, date, content, article_path)


def read_articles(dir_path: str,
                  extension: str = 'md',
                  trace_on: bool = False) -> List[Article]:

    # 指定した拡張子のファイルを探す
    glob_pattern: str = os.path.join(dir_path, f'*.{extension}')
    file_paths: List[str] = glob.glob(glob_pattern)

    # それらのファイルを読み込む
    articles: List[Article] = []
    for file_path in file_paths:
        articles.append(read_article(file_path, trace_on))

    return articles
