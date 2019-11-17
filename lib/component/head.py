def _gen_title(title_str: str) -> str:
    return '<title>' + title_str + '</title>'


def _gen_styles(root: str) -> str:
    html: str = '<link rel="stylesheet" href="' + root + 'css/reset.css">'
    html += '<link rel="stylesheet" href="' + root + 'css/style.css">'
    return html


def _gen_highlight(root: str) -> str:
    html: str = '<link rel="stylesheet" href="' + root + 'css/vs.css">'
    html += '<script src="' + root + 'js/highlight.pack.js"></script>'
    html += '<script>hljs.initHighlightingOnLoad();</script>'
    return html


def _gen_katex() -> str:
    html: str = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/katex.min.css" integrity="sha384-dbVIfZGuN1Yq7/1Ocstc1lUEm+AT+/rCkibIcC/OmWo5f0EA48Vf8CytHzGrSwbQ" crossorigin="anonymous">'
    html += '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/katex.min.js" integrity="sha384-2BKqo+exmr9su6dir+qCw08N2ZKRucY4PrGQPPWU1A7FtlCGjmEGFqXCv5nyM5Ij" crossorigin="anonymous"></script>'
    html += '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous" onload="renderMathInElement(document.body, {delimiters: [{left: \'$$\', right: \'$$\', display: true}, {left: \'$\', right: \'$\', display: false}]});"></script>'
    return html


def gen(root: str, title_str: str) -> str:
    html: str = '<head>'
    html += '<meta charset="UTF-8">'
    html += _gen_title(title_str)
    html += _gen_styles(root)
    html += _gen_highlight(root)
    html += _gen_katex()
    html += '</head>'
    return html
