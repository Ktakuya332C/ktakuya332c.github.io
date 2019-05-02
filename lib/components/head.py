# Head generator

def gen_title():
  return '<title>' + 'Principles' + '</title>'

def gen_styles(root):
  return '\n'.join([
    '<link rel="stylesheet" href="' + root + 'css/reset.css">',
    '<link rel="stylesheet" href="' + root + 'css/style.css">'
  ])

def gen_highlight(root):
  return '\n'.join([
    '<link rel="stylesheet" href="' + root + 'css/vs.css">',
    '<script src="' + root + 'js/highlight.pack.js"></script>',
    '<script>hljs.initHighlightingOnLoad();</script>',
  ])

def gen_katex():
  return '\n'.join([
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/katex.min.css" integrity="sha384-dbVIfZGuN1Yq7/1Ocstc1lUEm+AT+/rCkibIcC/OmWo5f0EA48Vf8CytHzGrSwbQ" crossorigin="anonymous">',
    '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/katex.min.js" integrity="sha384-2BKqo+exmr9su6dir+qCw08N2ZKRucY4PrGQPPWU1A7FtlCGjmEGFqXCv5nyM5Ij" crossorigin="anonymous"></script>',
    '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous" onload="renderMathInElement(document.body, {delimiters: [{left: \'$$\', right: \'$$\', display: true}, {left: \'$\', right: \'$\', display: false}]});"></script>'
  ])

def gen(highlight=True, katex=True, root=True):
  root = '' if root else '../'
  content = '<meta charset="UTF-8">\n'
  content += gen_title() + '\n'
  content += gen_styles(root) + '\n'
  if highlight: content += gen_highlight(root) + '\n'
  if katex: content += gen_katex() + '\n'
  return '<head>\n' + content + '</head>'
