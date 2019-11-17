import os
import glob
import codecs
from lib import article, top

def gen_index(articles):
  fout = codecs.open(INDEX_HTML, 'w')
  fout.write(top.gen(articles))
  fout.close()

def gen_articles():
  if not os.path.exists(BUILD_DIR): os.makedirs(BUILD_DIR)
  paths = glob.glob(os.path.join(ARTICLE_DIR, '*.md'))
  articles = list()
  for path in paths:
    # Read meta info
    fin = codecs.open(path, 'r')
    title_str = fin.readline()
    date_str = fin.readline()
    content = fin.read()
    
    # Compile article
    print("Compiling {}".format(path))
    f_name = os.path.basename(path)
    f_name = f_name.replace('.md', '.html')
    build_path = os.path.join(BUILD_DIR, f_name)
    fout = codecs.open(build_path, 'w')
    fout.write(article.gen(title_str, date_str, content))
    fout.close()
    
    # Store article info
    year = date_str.split('-')[0]
    date = '-'.join(date_str.split('-')[1:])
    articles.append(article.Article(year, date, title_str, path, build_path))
  
  return articles

def main():
  articles = gen_articles()
  gen_index(articles)

if __name__ == "__main__":
  INDEX_HTML = "index.html"
  ARTICLE_DIR = "articles"
  BUILD_DIR = "build"
  main()

