# A compiler of Markdown Documents
from lib.compiler import prefix
from lib.compiler import inline

def gen(pmd_text):
  p_texts = pmd_text.strip('\n').split('\n\n\n')
  pmd_html_list = list()
  for p_text in p_texts:
    prefix_html, content_text, suffix_html = prefix.process(p_text)
    content_html = inline.process(content_text)
    if content_html:
      pmd_html_list.append(prefix_html + content_html + suffix_html)
  pmd_html = '\n'.join(pmd_html_list)
  return pmd_html