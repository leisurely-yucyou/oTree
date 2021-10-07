# oTree
以下の実験プログラムがあります。
- 共通価値オークション(common value auction)
- 今後追加

使い方は、各プログラムのフォルダをsettings.pyやmanage.pyのあるフォルダ(下の画像みたいなところ)に追加することで使えます。

![スクリーンショット 2021-03-18 221853](https://user-images.githubusercontent.com/48300561/111633967-5fff1c80-8839-11eb-8515-6d8a564c013e.png)

## 各ファイルについての説明

### settings.py
まずSESSION_CONFIGSについて
~~~
SESSION_CONFIGS = [
    dict(
        name = '実験プログラムの名前',
        display_name = '被験者に表示する実験の名前',
        num_demo_participants = 5, #デモプレイを行うときの被験者数
        app_sequence=['実験プログラムのフォルダ名'] 
    ),
]
~~~
nameでは実験プログラムの名前を設定し、display_nameでは被験者に表示する実験の名前を設定します。num_demo_paticipantsではプログラムをデモプレイする時の被験者数を設定します(実験本番には関係ない)。app_sequenceは対応する実験プログラムのフォルダ名を設定してください。

共通価値オークションの場合は次のようになります。
~~~
SESSION_CONFIGS = [
    dict(
        name = 'common_value_auction_S1',
        display_name = '共通価値オークション_S1',
        num_demo_participants = 5,
        app_sequence=['common_value_auction']
    ),
    dict(
        name = 'common_value_auction_S2',
        display_name = '共通価値オークション_S2',
        num_demo_participants = 10,
        app_sequence=['common_value_auction_10']
    ),
]
~~~
___

LAGUAGE_CODEでは実験の言語を設定します。
~~~
LANGUAGE_CODE = 'ja'
~~~
「ja」にすると日本語です。

___

次にお金の単位です。  
「JPY」にすることで日本円になります。  
REAL_WORLD_CURRENCY_DECIMAL_PLACESは小数点以下の桁数です。日本円では「0」でいいですが、ドルの場合には「2」などにするといいでしょう。  
USE_POINTSはTrueにすると単位が円やドルではなくポイントになります。Falseでいいでしょう。  
~~~
REAL_WORLD_CURRENCY_CODE = 'JPY'
REAL_WORLD_CURRENCY_DECIMAL_PLACES=0
USE_POINTS = False
~~~
___

次にROOMSの設定です。  
下の例は共通価値オークションの場合です。  

~~~
ROOMS = [
    dict(
    name='common_value_auction',
    display_name='共通価値オークション',
    participant_label_file='_rooms/common_value_auction.txt',
    use_secure_urls=False
    )
]
~~~

participant_label_fileで被験者のログインIDを設定するファイルを読み込みます。  
ちなみに上のコードで読み込んでいるファイルの_rooms/common_value_auction.txtの中身は次のようになっています。  
~~~
1  
2  
3  
~  中略
18  
19  
20  
~~~
事前に被験者にIDを割り当てるなら、_rooms/common_value_auction.txtの中身を書き換えましょう。  

___

DEBUGについては実験本番ではFalseにしておきましょう。  
ローカル環境でデモプレイをするときはTrueにするかコメントアウトで消しておく必要があります。  
~~~
DEBUG = False
~~~

___

ADMIN_USERNAME、ADMIN_PASSWORDは好きに設定してください。

~~~
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'economics2020'
~~~

___

