# Paragraph inline code processor tags

def _escape(code):
  """Escape characters incompatible with highlightjs"""
  code = code.replace('&', '&amp;')
  code = code.replace('"', '&quot;')
  code = code.replace("'", '&apos;')
  code = code.replace('<', '&lt;')
  code = code.replace('>', '&gt;')
  return code

def code_tag(code):
  code = _escape(code.strip())
  return '\n'.join([
    '<div class="code-container">',
      "<pre><code>" + code + "</code></pre>",
    '</div>'
  ])

def ul_tag(args):
  html = '<ul class="content-ul">'
  for arg in args:
    html += '<li class="content-ul-item">' + arg + '</li>'
  html += '</ul>'
  return html

def ol_tag(args):
  html = '<ol class="content-ol">'
  for arg in args:
    html += '<li class="content-ol-item">' + arg + '</li>'
  html += '</ol>'
  return html

def a_tag(text, link):
  return "<a href=\"" + link + "\">" + text + "</a>"

def def_tag(name, content):
  return '\n'.join([
    '<div class="content-def">',
      '<span class="content-def-name">' + name + '</span>',
      content,
    '</div>'
  ])

def rel_tag(url):
  if url[0] == '/':
    return '/build' + url
  else:
    return '/build/' + url

def emp_tag(text):
  return '<span class="inline-code">' + _escape(text.strip()) + '</span>'

def table_tag(args):
  assert len(args) > 1, "table must contain at least 2 or more rows"
  head = args[0].split(',')
  n_col = len(head)
  bodies = list()
  for arg in args[1:]:
    row = arg.split(',')
    assert len(row) == n_col, "Each row must have the same number of columns"
    bodies.append(row)
  
  content = '\n'.join(
    ['<table class="content-table">'] +
      ['\n'.join([
      '<tr class="content-tr">',
        '\n'.join([
          '<th class="content-th">' + elem + '</th>' for elem in head
        ]),
      '</tr>'])] +
      ['\n'.join([
      '<tr class="content-tr">',
        '\n'.join([
          '<td class="content-td">' + elem + '</td>' for elem in row
        ]),
      '</tr>']) for body in bodies] +
    ['</table>']
  )
  return content

def fig_tag(img_path):
  return '\n'.join([
    '<figure class="content-figure">',
      '<img class="content-img" src="' + img_path + '">',
    '</figure>'
  ])
