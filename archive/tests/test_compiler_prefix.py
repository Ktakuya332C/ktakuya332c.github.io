from unittest import TestCase
from lib.compiler import prefix

class TestCompilerPrefix(TestCase):
  
  def test_gen(self):
    # '#'のテスト
    p_text = "# これはタイトルです"
    res = prefix.process(p_text)
    self.assertEqual(res[1], "これはタイトルです")
    
    # '##'のテスト
    p_text = "## これはサブタイトルです"
    res = prefix.process(p_text)
    self.assertEqual(res[1], "これはサブタイトルです")
    
    # '>'のテスト
    p_text = "> これはquoteです"
    res = prefix.process(p_text)
    self.assertEqual(res[1], "これはquoteです")
    
    # デフォルトのテスト
    p_text = "これは通常の文章です"
    res = prefix.process(p_text)
    self.assertEqual(res[1], "これは通常の文章です")
