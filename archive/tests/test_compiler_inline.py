from unittest import TestCase
from lib.compiler import inline

class TestCompilerInline(TestCase):
  
  def test_process_tag_name(self):
    res_tag, res_len = inline.process_tag_name(
      "普通の文章の中に突然現るタグ\\tag{argument}をパースする", 14)
    self.assertEqual(res_tag, '\\tag')
    self.assertEqual(res_len, 4)
  
  def test_process_arguments(self):
    res_args, res_len = inline.process_arguments(
      "今回は\\tag{argument1}{argument2}{argument3}です", 7)
    self.assertEqual(len(res_args), 3)
    self.assertEqual(res_args[0], "argument1")
    self.assertEqual(res_args[1], "argument2")
    self.assertEqual(res_args[2], "argument3")
    self.assertEqual(res_len, 33)
    
    res_args, res_len = inline.process_arguments(
      "今回は\\tag{argument1\\tag{argument2}argument3}です", 7)
    self.assertEqual(len(res_args), 1)
    self.assertEqual(res_args[0], "argument1\\tag{argument2}argument3")
    self.assertEqual(res_len, 35)
  
  def test_process_macro(self):
    res_html, res_len = inline.process_macro(
      "今回は\\debug{普通の文章が中に入っている}場合のテストです", 3)
    self.assertEqual(res_html, "普通の文章が中に入っている")
    self.assertEqual(res_len, 21)
  
  def test_process_equation(self):
    res_html, res_len = inline.process_equation(
      "今回は$$ E = mc^2 $$です", 3)
    self.assertEqual(res_html, "$$ E = mc^2 $$")
    self.assertEqual(res_len, 14)
    
    res_html, res_len = inline.process_equation(
      "今回は$ S = 4 \pi r^2 $です", 3)
    self.assertEqual(res_html, "$ S = 4 \pi r^2 $")
    self.assertEqual(res_len, 17)
  
  def test_process(self):
    res_html = inline.process(
      "今回は$ l = 2\pi $と\debug{これはテスト}です")
    self.assertEqual(res_html, "今回は$ l = 2\pi $とこれはテストです")
