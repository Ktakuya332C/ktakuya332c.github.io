import textwrap


def gen(footer_str: str) -> str:
    return textwrap.dedent(f"""\
        <footer class="footer">
            <p class="copyright">{footer_str}</p>
        </footer>
    """)
