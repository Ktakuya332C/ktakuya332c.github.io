import os
import textwrap
from lib.entity.article import Article
from lib.component import head, header, footer


def gen(build_dir: str,
        root_path: str,
        title_str: str,
        desc_str: str,
        footer_str: str,
        article: Article) -> str:
    build_path = os.path.join("/", build_dir)
    head_block = head.gen(root_path, title_str)
    header_block = header.gen(build_path, title_str, desc_str)
    footer_block = footer.gen(footer_str)
    return textwrap.dedent(f"""\
        <!doctype html>
            <html lang="ja">
            {head_block}
            <body>
                <div class="container">
                    {header_block}
                    <hr class="border">
                    <main class="main">
                        <div class="article-wrapper">
                            <div class="header">
                                <h2 class="title">{article.name}</h2>
                                <p class="date">{article.date}</h2>
                            </div>
                            <div class="content">
                                {article.content}
                            </div>
                        </div>
                    </main>
                    <hr class="border">
                    {footer_block}
                </div>
            </body>
        </html>
    """)
