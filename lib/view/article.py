import textwrap
from lib.entity.article import Article
from lib.component import head, header, footer


def gen(root: str,
        title_str: str,
        desc_str: str,
        footer_str: str,
        article: Article) -> str:
    head_block = head.gen(root, title_str)
    header_block = header.gen(title_str, desc_str)
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
