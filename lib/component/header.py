import textwrap


def gen(build_dir: str, title_str: str, desc_str: str) -> str:
    return textwrap.dedent(f"""\
        <header class="header">
            <h1 class="logo">
                <a href="{build_dir}">{title_str}</a>
            </h1>
            <p class="desc">{desc_str}</a>
        </header>
    """)
