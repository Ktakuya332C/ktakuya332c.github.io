import sys
from typing import List, Callable
from lib.errors import CompileError
from lib.compiler.functions import FuncType, FuncMapType
from lib.compiler.functions import default_func_map, root_func


class Converter:

    text: str
    text_length: int
    cursor: int
    func_map: FuncMapType

    def __init__(self,
                 text: str,
                 trace_on: bool = False,
                 func_map: FuncMapType = default_func_map):
        self.text = text
        self.text_length = len(text)
        self.cursor = 0
        self.trace_on = trace_on
        self.func_map = func_map

    def execute(self):
        self.text = '{' + self.text + '}'
        self.text_length = len(self.text)
        content: str = self._convert()
        if self.cursor != self.text_length:
            raise CompileError('全てのテキストを読み終わっているはずですが、まだ読み残しがあります')
        return content

    def _convert(self,
                 func: FuncType = root_func,
                 interpret_args: bool = True) -> str:
        args: List[str] = []
        if self.trace_on:
            print(f'{func.__name__}関数を呼び出します', file=sys.stderr)
        while(self._exist_arg()):
            if self.trace_on:
                print('引数のパースを始めます', file=sys.stderr)
            arg: str = self._read_arg() if interpret_args else self._read_arg_verbatim()
            if self.trace_on:
                print('次の引数を読み取ることができました', file=sys.stderr)
                print(arg, file=sys.stderr)
            args.append(arg)
        return func(args)

    def _exist_arg(self) -> bool:
        lookahead: int = self.cursor
        while(lookahead < self.text_length and self.text[lookahead].isspace()):
            lookahead += 1
        if lookahead == self.text_length:
            return False
        else:
            return (self.text[lookahead] == '{')

    def _read_arg(self) -> str:

        # 開始記号の前にあるかもしれない空白などを読み飛ばす
        if self.cursor >= self.text_length:
            raise CompileError('すでにテキストは終了しているので、引数はもう存在しません')
        while(self.text[self.cursor].isspace()):
            self.cursor += 1

        # 引数の開始記号'{'が存在することが期待されている
        cur_text: str = self.text[self.cursor]
        if cur_text != '{':
            raise CompileError(f'引数の開始記号ではなく{cur_text}が検知されました')
        self.cursor += 1

        # 引数の中身を読み進める
        content: str = ''
        while(self.cursor < self.text_length and self.text[self.cursor] != '}'):
            if self.text[self.cursor] == '@':
                self.cursor += 1
                f_name: str = ''
                while(self.text[self.cursor].isalnum()):
                    f_name += self.text[self.cursor]
                    self.cursor += 1
                if f_name not in self.func_map:
                    raise CompileError(f'関数{f_name}は存在しません')
                func, interpret_args = self.func_map[f_name]
                content += self._convert(func, interpret_args)
            else:
                content += self.text[self.cursor]
                self.cursor += 1

        # 先のループが終端記号'}'を検知して終わったことを確認する
        if self.cursor >= self.text_length:
            raise CompileError('引数の終端記号の前にテキストが終了してしまいました')

        # 引数の終端記号'}'が存在することが期待されている
        cur_text = self.text[self.cursor]
        if cur_text != '}':
            raise CompileError(f'引数の終端記号ではなく{cur_text}が検知されました')
        self.cursor += 1

        return content.strip()

    def _read_arg_verbatim(self) -> str:

        # カウンターを初期化する
        counter: int = 0

        # 開始記号の前にあるかもしれない空白などを読み飛ばす
        if self.cursor >= self.text_length:
            raise CompileError('すでにテキストは終了しているので、引数はもう存在しません')
        while(self.text[self.cursor].isspace()):
            self.cursor += 1

        # 引数の開始記号'{'が存在することが期待されている
        cur_text: str = self.text[self.cursor]
        if cur_text != '{':
            raise CompileError(f'引数の開始記号ではなく{cur_text}が検知されました')
        self.cursor += 1
        counter += 1

        # 引数の中身を解釈せずに読み進める
        content: str = ''
        while(counter > 0):
            if self.cursor >= self.text_length:
                raise CompileError('引数の終端記号が現れる前にテキストが終了してしまいました')
            if self.text[self.cursor] == '{':
                counter += 1
            elif self.text[self.cursor] == '}':
                counter -= 1
            content += self.text[self.cursor]
            self.cursor += 1

        # 最後尾の'}'だけ消しておく
        cur_text = content[-1]
        if cur_text != '}':
            raise CompileError(f'引数の終端記号ではなく{cur_text}が検知されました')
        content = content[:-1]

        return content.strip()
