import os
import sys
import shutil
from lib.main import main
from lib.errors import BlogError

article_dir = 'articles_en'
build_dir = 'build_en'
index_file = 'index.html'
root_path = '/'
title_str = 'Memorandum'
desc_str = 'My personal notes'
footer_str = 'Copyright@2022 Ktakuya. All rights reserved.'
trace_on = False
try:
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    main(index_file,
         article_dir,
         build_dir,
         root_path,
         title_str,
         desc_str,
         footer_str,
         trace_on)
except BlogError as e:
    print('エラーが起きました。エラー内容は以下を参照してください', file=sys.stderr)
    print('----', file=sys.stderr)
    print(e.reason, file=sys.stderr)
    sys.exit(1)
