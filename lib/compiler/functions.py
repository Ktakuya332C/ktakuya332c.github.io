from typing import Callable, List, Dict, Tuple
from lib.errors import CompileError

FuncType = Callable[[List[str]], str]
FuncMapType = Dict[str, Tuple[FuncType, bool]]


def _assert_n_args(name: str, args: List[str], n_args):
    if len(args) == n_args:
        return
    error_msg: str = ''
    error_msg += f'{name}関数は引数を{n_args}つ期待していましたが、{len(args)}こ渡されました\n'
    error_msg += '現在渡されている引数は以下になります\n'
    for cnt, arg in enumerate(args):
        error_msg += f'引数{cnt+1}こ目: {arg}\n'
    raise CompileError(error_msg)


def _escape(code: str) -> str:
    code = code.replace('&', '&amp;')
    code = code.replace('"', '&quot;')
    code = code.replace("'", '&apos;')
    code = code.replace('<', '&lt;')
    code = code.replace('>', '&gt;')
    return code

# ----
# root関数
# ----


def root_func(args: List[str]) -> str:
    _assert_n_args('root', args, 1)
    return args[0]


# ----
# inline関数
# ----

def a_func(args: List[str]) -> str:
    _assert_n_args('a', args, 2)
    return '<a href="' + args[1] + '">' + args[0] + '</a>'


def incode_func(args: List[str]) -> str:
    _assert_n_args('incode', args, 1)
    code: str = _escape(args[0])
    return '<span class="inline-code">' + code + '</span>'


def rel_func(args: List[str]) -> str:
    _assert_n_args('rel', args, 1)
    path: str = args[0]
    if path[0] == '/':
        return f'..{path}'  # TODO: 後で綺麗にするべき
    else:
        return f'../{path}'  # TODO: 後で綺麗にするべき


def inmath_func(args: List[str]) -> str:
    _assert_n_args('inmath', args, 1)
    return '$' + args[0] + '$'

# ----
# block関数
# ----


def p_func(args: List[str]) -> str:
    _assert_n_args('p', args, 1)
    return '<p class="content-paragraph">' + args[0] + '</p>'


def blcode_func(args: List[str]) -> str:
    _assert_n_args('blcode', args, 1)
    code: str = _escape(args[0])
    return '<div class="code-container"><pre><code>' + code + '</code></pre></div>'


def ul_func(args: List[str]) -> str:
    html: str = '<ul class="content-ul">'
    for arg in args:
        html += '<li class="content-ul-item">' + arg + '</li>'
    html += '</ul>'
    return html


def ol_func(args: List[str]) -> str:
    html: str = '<ol class="content-ol">'
    for arg in args:
        html += '<li class="content-ol-item">' + arg + '</li>'
    html += '</ol>'
    return html


def def_func(args: List[str]) -> str:
    _assert_n_args('def', args, 2)
    html: str = '<div class="content-def">'
    html += '<p><span class="content-def-name">' + args[0] + '</span></p>'
    html += args[1]
    html += '</div>'
    return html


def fig_func(args: List[str]) -> str:
    _assert_n_args('fig', args, 1)
    html: str = '<figure class="content-figure">'
    html += '<img class="content-img" src="' + args[0] + '">'
    html += '</figure>'
    return html


def table_func(args: List[str]) -> str:
    if len(args) < 1:
        raise CompileError(
            f'table関数は引数を一つ以上期待していましたが、{len(args)}こしか渡されませんでした')

    html: str = '<table class="content-table">'

    # ヘッダー要素を追加
    html += '<tr class="content-tr">'
    head_elems: List[str] = args[0].split(',')
    for head_elem in head_elems:
        html += '<th class="content-th">' + head_elem + '</th>'
    html += '</tr>'

    # 各列の要素を追加
    for row in args[1:]:
        elems: List[str] = row.split(',')
        if len(elems) != len(head_elems):
            raise CompileError(f'table関数に渡される各列は同じ数の行を持つ必要があります')
        html += '<tr class="content-tr">'
        for elem in elems:
            html += '<td class="content-td">' + elem + '</td>'
        html += '</tr>'

    html += '</table>'
    return html


def section_func(args: List[str]) -> str:
    _assert_n_args('rel', args, 1)
    return '<h1 class="section-title">' + args[0] + '</h1>'


def subsection_func(args: List[str]) -> str:
    _assert_n_args('rel', args, 1)
    return '<h1 class="subsection-title">' + args[0] + '</h1>'


def blmath_func(args: List[str]) -> str:
    _assert_n_args('blmath', args, 1)
    return '$$' + args[0] + '$$'


def quote_func(args: List[str]) -> str:
    _assert_n_args('quote', args, 1)
    return '<p class="content-quote">' + args[0] + '</p>'


# ----
# それぞれの関数名について、その実際の関数とその関数が引数を解釈するかどうかを表す真偽値を対応させる辞書
# ----
default_func_map: FuncMapType = {
    'a': (a_func, True),
    'p': (p_func, True),
    'incode': (incode_func, False),
    'blcode': (blcode_func, False),
    'ul': (ul_func, True),
    'ol': (ol_func, True),
    'def': (def_func, True),
    'fig': (fig_func, True),
    'table': (table_func, True),
    'rel': (rel_func, True),
    'section': (section_func, True),
    'subsection': (section_func, True),
    'inmath': (inmath_func, False),
    'blmath': (blmath_func, False),
    'quote': (quote_func, True),
}
