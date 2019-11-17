# Header generator

def gen():
  return '\n'.join([
    '<header class="header">',
      '<h1 class="logo">',
        '<a href="/">Principles</a>',
      '</h1>',
      '<p class="desc">エンジニアKtakuyaのブログ</p>',
    '</header>'
  ])