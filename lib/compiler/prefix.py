# Paragraph prefix processor

from lib.compiler.prefix_tags import (
    section_title, subsection_title, quote, default)

def process(p_text):
  splitted = p_text.split(' ')
  prefix_cand = splitted[0]
  content_cand = ' '.join(splitted[1:])
  
  if prefix_cand == '#':
    tag_before, tag_after = section_title()
    return tag_before, content_cand, tag_after
  elif prefix_cand == '##':
    tag_before, tag_after = subsection_title()
    return tag_before, content_cand, tag_after
  elif prefix_cand == '>':
    tag_before, tag_after = quote()
    return tag_before, content_cand, tag_after
  else:
    tag_before, tag_after = default()
    return tag_before, p_text, tag_after
