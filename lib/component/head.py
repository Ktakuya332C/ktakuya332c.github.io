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
    html: str = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css" integrity="sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq" crossorigin="anonymous">'
    html += '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.js" integrity="sha384-y23I5Q6l+B6vatafAwxRu/0oK/79VlbSz7Q9aiSZUvyWYIYsd+qj+o24G5ZU2zJz" crossorigin="anonymous"></script>'
    html += '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous" onload="renderMathInElement(document.body, {delimiters: [{left: \'$$\', right: \'$$\', display: true}, {left: \'$\', right: \'$\', display: false}]});"></script>'
    return html


def _gen_google_analytics() -> str:
    html: str = '<script async src="https://www.googletagmanager.com/gtag/js?id=UA-164492761-1"></script>'
    html += '<script>'
    html += 'window.dataLayer = window.dataLayer || [];'
    html += 'function gtag(){dataLayer.push(arguments);}'
    html += 'gtag("js", new Date());'
    html += 'gtag("config", "UA-164492761-1");'
    html += '</script>'
    return html


def gen(root: str, title_str: str) -> str:
    html: str = '<head>'
    html += '<meta charset="UTF-8">'
    html += _gen_google_analytics()
    html += _gen_title(title_str)
    html += _gen_styles(root)
    html += _gen_highlight(root)
    html += _gen_katex()
    html += '</head>'
    return html
