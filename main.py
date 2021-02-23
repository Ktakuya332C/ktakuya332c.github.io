import os
import sys
import shutil
from lib.main import main
from lib.errors import BlogError

article_dir = 'articles'
build_dir = 'build'
root_from_build = '../'
index_path = 'index.html'
root_from_index = './'
title_str = 'Preloading'
desc_str = 'Ktakuyaのブログ'
footer_str = 'Copyright@2021 Ktakuya. All rights reserved.'
trace_on = False
try:
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    main(article_dir,
         build_dir,
         root_from_build,
         index_path,
         root_from_index,
         title_str,
         desc_str,
         footer_str,
         trace_on)
except BlogError as e:
    print('エラーが起きました。エラー内容は以下を参照してください', file=sys.stderr)
    print('----', file=sys.stderr)
    print(e.reason, file=sys.stderr)
    sys.exit(1)
