# coding: UTF-8

def get_response(targetURL, waitsec_from=1, waitsec_to=3):
    #ヘッダー情報
    headers =  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    #リクエストを送信
    response = requests.get(targetURL, headers=headers)
    #文字化け対策
    response.encoding = cchardet.detect(response.content)["encoding"]
    msg_headder = "from cache"
    if not repython setup.py develop -usponse.from_cache: #response.from_cache: キャッシュに対してリクエストを送っていたらTrueを返す
        s = randint(waitsec_from,waitsec_to) #randint(任意の範囲のランダムな整数を生成)
        time.sleep(s)#指定秒数処理を停止させる
        msg_headder = 'random sleep ' + str(s) + 'sec'
        #print()の書式,file引数に指定した先へ出力することが可能(requests.logファイルに出力)
    print(str(datetime.datetime.now()) + ',' + msg_headder + ',' + response.url, file=codecs.open('requests.log', 'a', 'utf-8'))
    return response
