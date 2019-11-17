import unittest
from lib.errors import CompileError
from lib.compiler.converter import Converter


class TestConverter(unittest.TestCase):

    def test_exist_arg(self):

        # 正常系
        cases_true = [
            '{これはテストです}',
            '  {これはテストです}',
            '\t{これはテストです}',
            '\n{これはテストです}',
            '{これはテスト',
            '  {これはテスト',
            '\t{これはテスト',
            '\n{これはテスト',
        ]
        for text in cases_true:
            target = Converter(text, func_map=None)
            self.assertTrue(target._exist_arg(), f'{text}の場合が失敗しました')

        # 異常系
        cases_false = [
            '',
            'これはテストです',
            'テスト{これはテストです}',
            ' テスト{これはテストです}',
            '}これはテスト',
            'テスト}これはテスト',
            ' テスト}これはテスト'
        ]
        for text in cases_false:
            target = Converter(text, func_map=None)
            self.assertFalse(target._exist_arg(), f'{text}の場合が失敗しました')

        # 冪等性
        target = Converter('{これはテストです}', func_map=None)
        for _ in range(3):
            self.assertTrue(target._exist_arg(), f'{text}の場合が失敗しました')

    def test_read_arg_verbatim(self):

        # 正常系
        cases_normal = [
            ('{これはテストです}', 'これはテストです'),
            ('{ これはテストです }', 'これはテストです'),
            ('{\tこれはテストです }', 'これはテストです'),
            ('{\nこれはテストです\n}', 'これはテストです'),
            ('{これは{テスト}です}', 'これは{テスト}です'),
            (' {これは{テスト}です} ', 'これは{テスト}です'),
            ('\t{これは{テスト}です} ', 'これは{テスト}です'),
            ('\n{これは{テスト}です} ', 'これは{テスト}です'),
            (r'{これは@math{\sum_{n=1}^{10} n = 55}です}', r'これは@math{\sum_{n=1}^{10} n = 55}です')
        ]
        for text, expected in cases_normal:
            target = Converter(text, func_map=None)
            self.assertEqual(target._read_arg_verbatim(), expected)

        # 異常系
        cases_error = [
            '',
            '{これはテストです',
            ' {これはテストです',
            'テスト{これはテストです}',
            ' テスト{これはテストです}',
            '}これはテストです',
            ' }これはテストです',
        ]
        for text in cases_error:
            target = Converter(text, func_map=None)
            with self.assertRaises(CompileError):
                target._read_arg_verbatim()

    def test_read_arg(self):
        func_map = {
            'a': (lambda args: f'<a></a>', True),
            'b': (lambda args: f'<b>{args[0]}</b>', True),
            'c': (lambda args: f'<c>{args[0]}</c>', False)
        }

        # 正常系
        cases_normal = [
            ('{これはテストです}', 'これはテストです'),
            (' {これはテストです} ', 'これはテストです'),
            (' { これはテストです\t} ', 'これはテストです'),
            (' {\nこれはテストです} ', 'これはテストです'),
            ('{これは @a です}', 'これは <a></a> です'),
            ('\t{これは @a です} ', 'これは <a></a> です'),
            ('{これは@b{これはテスト}です}', 'これは<b>これはテスト</b>です'),
            ('{これは@b{\n これはテスト\t}です}', 'これは<b>これはテスト</b>です'),
            ('{これは@b{これは @a テスト}です}', 'これは<b>これは <a></a> テスト</b>です'),
            ('{これは@c{これは{かっこ}テスト}です}', 'これは<c>これは{かっこ}テスト</c>です'),
        ]
        for text, expected in cases_normal:
            target = Converter(text, func_map=func_map)
            self.assertEqual(target._read_arg(), expected)

        # 異常系
        cases_error = [
            '',
            '{',
            ' {',
            ' { ',
            '}',
            'これはテストです',
            '{これはテストです',
            'これは{これはテストです}',
            '{これは @aです}'
        ]
        for text in cases_error:
            target = Converter(text, func_map=func_map)
            with self.assertRaises(CompileError):
                target._read_arg()

    def test_convert(self):

        # _read_args関数でほとんどテスト済みなので、簡単な正常系のみ
        target = Converter('{これはテストです}', func_map=None)
        self.assertEqual(target._convert(), 'これはテストです')

    def test_execute(self):
        target = Converter('これはテストです', func_map=None)
        self.assertEqual(target.execute(), 'これはテストです')


if __name__ == '__main__':
    unittest.main()
