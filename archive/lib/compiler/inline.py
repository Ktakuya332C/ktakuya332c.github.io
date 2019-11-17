# Paragraph inline code processor
import sys
import string
from lib.compiler.error import ParseError
from lib.compiler.inline_tags import (
    code_tag, ul_tag, a_tag, def_tag, ol_tag,
    rel_tag, emp_tag, table_tag, fig_tag)

def assert_in_range(content_text, cur, peek, name):
  if peek >= len(content_text):
    raise ParseError(
      'Failed to parse {}: {}'.format(name, content_text[cur:]))

def process_tag_name(content_text, cur):
  peek = cur + 1
  while(content_text[peek] != '{'):
    peek += 1
    assert_in_range(content_text, cur, peek, 'tag name')
  tag_name = content_text[cur:peek].strip()
  return tag_name, peek - cur

def process_arguments(content_text, cur):
  peek = cur
  in_arg = False
  surplus = 0
  args = list()
  entries = "{}" + string.whitespace
  while peek < len(content_text) and (in_arg or content_text[peek] in entries):
    if content_text[peek] == '{':
      if in_arg:
        surplus += 1
        arg += content_text[peek]
      else:
        arg = ""
        in_arg = True
    elif content_text[peek] == '}':
      if surplus > 0:
        surplus -= 1
        arg += content_text[peek]
      else:
        args.append(arg)
        in_arg = False
    elif in_arg:
      arg += content_text[peek]
    
    peek += 1
  
  if in_arg: assert_in_range(content_text, cur, peek, 'tag arguments')
  return args, peek - cur

def process_macro(content_text, cur):
  peek = cur
  
  # Get the tag name
  tag_name, sub_num = process_tag_name(content_text, peek)
  peek += sub_num
  
  # Get all arguments
  args, sub_num = process_arguments(content_text, peek)
  peek += sub_num
  
  # Process macro
  html = ""
  if tag_name == '\\debug':
    assert len(args) == 1, "\\debug takes only 1 argument, got {}".format(args)
    html = args[0]
  elif tag_name == '\\code':
    assert len(args) == 1, "\\code takes only 1 argument, got {}".format(args)
    html = code_tag(args[0])
  elif tag_name == '\\ul':
    for i in range(len(args)): args[i] = process(args[i])
    html = ul_tag(args)
  elif tag_name == '\\a':
    assert len(args) == 2, "\\a takes only 2 arguments, got {}".format(args)
    for i in range(len(args)): args[i] = process(args[i])
    html = a_tag(args[0], args[1])
  elif tag_name == '\\def':
    assert len(args) == 2, "\\def takes only 2 arguments, got {}".format(args)
    for i in range(len(args)): args[i] = process(args[i])
    html = def_tag(args[0], args[1])
  elif tag_name == '\\ol':
    for i in range(len(args)): args[i] = process(args[i])
    html = ol_tag(args)
  elif tag_name == '\\rel':
    assert len(args) == 1, "\\ref takes only 1 argument, got {}".format(args)
    html = rel_tag(args[0])
  elif tag_name == '\\emp':
    assert len(args) == 1, "\\emp takes only 1 argument, got {}".format(args)
    html = emp_tag(args[0])
  elif tag_name == '\\table':
    for i in range(len(args)): args[i] = process(args[i])
    html = table_tag(args)
  elif tag_name == '\\fig':
    assert len(args) == 1, "\\fig takes only 1 arguments, got {}".format(args)
    html = fig_tag(args[0])
  else:
    raise ParseError('Unknown macro found: {}'.format(tag_name))
  return html, peek - cur

def process_equation(content_text, cur):
  
  # Display mode $$ ~ $$
  if content_text[cur:cur+2] == '$$':
    peek = cur + 2
    while(content_text[peek:peek+2] != '$$'):
      peek += 1
      assert_in_range(content_text, cur, peek, 'display equation')
    peek += 2
    return content_text[cur:peek], peek - cur
  
  # Inline mode $ ~ $
  elif content_text[cur] == '$':
    peek = cur + 1
    while(content_text[peek] != '$'):
      peek += 1
      assert_in_range(content_text, cur, peek, 'inline equation')
    peek += 1
    return content_text[cur:peek], peek - cur

def process(content_text, top_level=False):
  cur = 0
  html = ""
  while cur < len(content_text):
    if content_text[cur] == '\\':
      sub_html, sub_num = process_macro(content_text, cur)
      html += sub_html
      cur += sub_num
    elif content_text[cur] == '$':
      sub_html, sub_num = process_equation(content_text, cur)
      html += sub_html
      cur += sub_num
    else:
      html += content_text[cur]
      cur += 1
  return html
