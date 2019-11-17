import textwrap


def gen(title_str: str, desc_str: str) -> str:
    return textwrap.dedent(f"""\
        <header class="header">
            <h1 class="logo">
                <a href="/">{title_str}</a>
            </h1>
            <p class="desc">{desc_str}</a>
        </header>
    """)
