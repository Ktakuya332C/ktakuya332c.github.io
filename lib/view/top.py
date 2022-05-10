import os
import textwrap
from typing import List
from operator import attrgetter
from lib.entity.article import Article
from lib.component import head, header, footer


def _gen_content(article: Article, build_path: str, insert_year: bool = False):
    year: str = article.date.strftime('%Y')
    year_or_empty: str = year if insert_year else ''
    month_day: str = article.date.strftime('%m-%d')
    file_name: str = article.file_name()
    path: str = os.path.join(build_path, f'{file_name}.html')
    return textwrap.dedent(f"""\
        <li class="article-item">
            <a href="{path}">
                <span class="year">{year_or_empty}</span>
                <span class="date">{month_day}</span>
                <span class="title">{article.name}</span>
            </a>
        </li>
    """)


def _gen_contents(articles: List[Article], build_dir: str):
    articles = sorted(articles, key=attrgetter('date'), reverse=True)
    html: str = '<ul class="article-list">'
    prev_year: int = -1
    for article in articles:
        html += _gen_content(article, build_dir,
                             prev_year != article.date.year)
        prev_year = article.date.year
    html += '</ul>'
    return html


def gen(build_dir: str,
        root_path: str,
        title_str: str,
        desc_str: str,
        footer_str: str,
        articles: List[Article]):
    build_path = os.path.join("/", build_dir)
    head_block = head.gen(root_path, title_str)
    header_block = header.gen(build_path, title_str, desc_str)
    footer_block = footer.gen(footer_str)
    contents = _gen_contents(articles, build_path)
    return textwrap.dedent(f"""\
        <!doctype html>
        <html lang="ja">
        {head_block}
        <body>
            <div class="container">
                {header_block}
                <hr class="border">
                <main class="main">
                    {contents}
                </main>
                <hr class="border">
                {footer_block}
            </div>
        </body>
        </html>
    """)
