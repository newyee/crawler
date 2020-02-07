クローリングする際、サーバーに負荷をかけないよう一度アクセスしたページをキャッシュし、
``requests_cache.install_cache`` に指定した時間、ローカルに保存したURLを介してアクセスを行う。

SAMPLE
======================== 
::

  from response.crawler import get_response
  from bs4 import BeautifulSoup
  import requests
  import datetime
  import cchardet
  import requests_cache
  #クローリング対象のURL
  target_url = 'test.co.jp'
  #キャッシュの有効化
  requests_cache.install_cache(cache_name='test_cache', backend='sqlite', expire_after=60*120)
  soup = BeautifulSoup(get_response(targetURL).content,'lxml')
  print(soup)