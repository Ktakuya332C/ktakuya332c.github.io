# Paragraph prefix processor tags

def section_title():
  return '<h1 class="section-title">', '</h1>'

def subsection_title():
  return '<h1 class="subsection-title">', '</h1>'

def quote():
  return '<div class="content-quote"><p>', '</p></div>'

def default():
  return '<div class="content-paragraph">', '</div>'
