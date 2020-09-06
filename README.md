IR Remote API
=============

Bit Trade One の赤外線リモコンをRESTfulっぽいAPIから使えるようにするAPIサーバーのようなもの。
内部で"kjmkznr/bto_ir_cmd"を呼び出してます。

## Requirement

* kjmkznr/bto_ir_cmd
* Python 3.6.5
* Flask


## install

Flaskで動いているのでFlaskのインストールが必要です。
~~~
$ pip install Flask
$ git clone https://github.com/nnnamani/ir_remote_api.git
~~~

Bit Trade Oneの赤外線リモコンをコマンドラインから操作できるようにするツール
"kjmkznr/bto_ir_cmd"をインストールします。


conf.pyのIR_CMDに"bto_ir_cmd"へのパスを設定します。
"ir_code"には、リモコンで操作する対象とその対象を操作する赤外線コードを設定します。
以下の例では、LIGHTに対して、'ON'と'OFF'という操作を定義しています。

~~~
$ cd ir_remote_api
$ cat conf.py
IR_CMD = "/home/pi/bin/bto_ir_cmd"

ir_code = [
    {
        'order': '1',
        'name'  : 'LIGHT',
        'codes' : [
            {
                'name' : 'ON',
                'code' : '82826DA6590000'
            },
            {
                'name' : 'OFF',
                'code' : '82826DBE410000'
            },
            {
.
.
.
~~~


サーバーを起動する
~~~
$ cd ir_remote_api
$ python app.py
* Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)
~~~


## 使いかた

http://localhost:3000/ir-remote/api/v1/light/on  => '82826DA6590000'が送信される
