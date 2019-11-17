import os
import glob
import codecs
from operator import attrgetter

from lib.article import Article
from lib.components import head
from lib.components import header
from lib.components import footer
from lib.compiler import compiler

def gen_content(article, year_on=True):
  year = article.year if year_on else ""
  return '\n'.join([
    '<li class="article-item">',
      '<a href="{}">'.format(article.build_path),
        '<span class="year">' + year + '</span>',
        '<span class="date">' + article.date + '</span>',
        '<span class="title">' + article.title + '</span>',
      '</a>',
    '</li>'
  ])

def gen(articles):
  articles = sorted(articles, key=attrgetter('date'), reverse=True)
  articles = sorted(articles, key=attrgetter('year'), reverse=True)
  
  contents = list()
  prev_year = -1
  for article in articles:
    contents.append(gen_content(article, article.year != prev_year))
    prev_year = article.year
  
  return "\n".join([
    '<!DOCTYPE html>',
    '<html lang="ja">',
      head.gen(),
      '<body>',
        '<div class="container">',
          header.gen(),
          '<hr class="border">',
          '<main class="main">',
            '<ul class="article-list">'] +
             contents +
            ['</ul>',
          '</main>',
          '<hr class="border">',
          footer.gen(),
        '</div>',
      '</body>',
    '</html>'
    ])
