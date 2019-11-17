import codecs
from collections import namedtuple

from lib.components import head
from lib.components import header
from lib.components import footer
from lib.compiler import compiler

Article = namedtuple(
  'Article',
  ('year', 'date', 'title', 'src_path', 'build_path')
)

def gen(title_str, date_str, content):
  return "\n".join([
    '<!DOCTYPE html>',
    '<html lang="ja">',
      head.gen(root=False),
      '<body>',
        '<div class="container">',
          header.gen(),
          '<hr class="border">',
          '<main class="main">',
            '<div class="article-wrapper">',
              '<div class="header">',
                '<h2 class="title">' + title_str + '</h2>',
                '<p class="date">' + date_str + '</p>',
              '</div>',
              '<div class="content">',
                compiler.gen(content),
              '</div>',
            '</div>',
          '</main>',
          '<hr class="border">',
          footer.gen(),
        '</div>',
      '</body>',
    '</html>'
    ])

