# PythonライブラリRichを試す

hackernewsでこんなライブラリが紹介されているのを見つけた
- [Rich is a Python library for rich text and beautiful formatting in the terminal.](https://github.com/willmcgugan/rich)

とりあえず試してみる。スクショを取りまくるのも面倒なので、色とか文字の装飾がメインなのでこのページでは表現できないので残念だが、`README.md`で紹介されているコードと少しを実際に書いてみた結果を貼っていってみる。


## Print
```
>>> from rich import print
>>> print("Hello, [bold magenta]World[/bold magenta]!")
Hello, World!
>>> print(locals())
{
    "Console": <class "rich.console.Console">,
    "__annotations__": {},
    "__builtins__": <module "builtins" (built-in)>,
    "__doc__": None,
    "__loader__": <class "_frozen_importlib.BuiltinImporter">,
    "__name__": "__main__",
    "__package__": None,
    "__spec__": None,
    "console": <console width=80 ColorSystem.EIGHT_BIT>,
    "print": <function print at 0x107ab7ca0>,
}
```

綺麗な色付けとフォーマットになるので、`pprint`よりも良いかもしれない。

## Console
```
>>> from rich.console import Console
>>> console = Console()
>>> console.print("Hello", "World", style="bold red")
Hello World
>>> console.print("[bold cyan]Bold Cyan[/bold cyan] [u]underline[/u] [i]italic[/i]")
Bold Cyan underline italic
>>> console.log("This is a pen")
[11:05:53] This is a pen
```


## Logging Handler
```
>>> import logging
>>> from rich.logging import RichHandler
>>> logger = logging.getLogger(__name__)
>>> logger.setLevel(logging.DEBUG)
>>> logger.addHandler(RichHandler())
>>> logger.info("Hello World")
[05/05/20 11:13:26] INFO     Hello World                               <stdin>:1
[05/05/20 11:13:26] INFO     INFO:__main__:Hello World                 <stdin>:
```


## Progress Bars
```
>>> import time
>>> from rich.progress import track
>>> for step in track(range(100)): time.sleep(1)
```


## Markdown
```
>>> import textwrap
>>> from rich.console import Console
>>> from rich.markdown import Markdown
>>> Console().print(Markdown(textwrap.dedent("""\
    # Title
    A simple explanation
    ## First section
    The content of the first section
    ## Second section
    The content of the second section
""")))
```


## Syntax
```
>>> import textwrap
>>> from rich.console import Console
>>> from rich.syntax import Syntax
>>> Console().print(Syntax(textwrap.dedent("""\
    def add_func(x, y):
        return x + y
"""), "python"))
```


## Tables
```
>>> from rich.console import Console
>>> from rich.table import Column, Table
>>> table = Table()
>>> table.add_column("Date")
>>> table.add_column("Title")
>>> table.add_row("Dev 20, 2019", "Star Wars: The Rise of Skywalker")
>>> table.add_row("May 25, 2018", "A Star Wars Story")
>>> Console().print(table)
```
