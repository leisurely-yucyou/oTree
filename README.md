# ExpEconの使い方

### 前提知識
- Anacondaがインストール済み 
- oTreeの基本的な使い方が分かる 
- oTreeがインストール済み 

上記がまだの場合
- Anacondaのインストール:こちらの[サイト](https://www.python.jp/install/anaconda/windows/install.html)を参照してインストールしてください
- oTreeのインストール:こちらの[サイト](https://otree.readthedocs.io/ja/latest/install-windows.html#install-windows)を参照してインストールしてください
- oTreeの基本的な使い方: こちらの[サイト](https://otree.readthedocs.io/ja/latest/tutorial/intro.html)を参照してください 

## 手順
1. まず、画像の右上のCodeボタン(緑色のボタン)をクリックしDwonload ZipからZipファイルをダウンロードします。  <br><br>
![image](https://user-images.githubusercontent.com/48300561/130906017-a06c47d4-ee15-4b82-b94a-7fdf239df275.png)

2. デスクトップなどにoTree用のフォルダを準備しておきます。
3. コマンドプロンプト等でカレントディレクトリを先ほど作ったoTree用のフォルダに設定する<br>
ステップ3がわからない場合は[こちら](https://github.com/leisurely-yucyou/oTree/blob/main/%E8%A3%9C%E8%B6%B3%E8%B3%87%E6%96%99/cmd%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6.md)
4. ``` otree startproject otreetest```をコマンドプロンプト等で打ち込む(otreetestの部分は任意のワードに変えてください)
5. 4番でoTree用フォルダ内にプロジェクトが出来たのでカレントディレクトリをそこに変更する
6. 先ほどダウンロードしたZipファイルを解凍しExpEconのフォルダ内のものをoTree用フォルダにコピーします。
<br>  

![image](https://user-images.githubusercontent.com/48300561/136321339-0966d4ee-365c-4705-a790-ccaa80d3d015.png)  

<br>  
上のファイルとフォルダをotree startprojectでできたフォルダ(下の画像のファイル等がある場所)へ移す。
<br>  

![image](https://user-images.githubusercontent.com/48300561/136321518-44416a6d-6868-442d-bf44-8c6eeb7fe371.png)  

<br>  

7. テキストエディタでsettings.pyを開きSESSION_CONFIGSとROOMSを次のように書き換えます。 
```
SESSION_CONFIGS = [
    dict(
        name = 'common_value_auction_S1',
        display_name = '共通価値オークション_S1',
        num_demo_participants = 5,
        app_sequence=['common_value_auction_5']
    ),
    dict(
        name = 'common_value_auction_S2',
        display_name = '共通価値オークション_S2',
        num_demo_participants = 10,
        app_sequence=['common_value_auction_10']
    ),
    dict(
        name = 'double_auction',
        display_name='ダブルオークション',
        num_demo_participants = 4,
        app_sequence=['double_auction']
    ),
    dict(
        name='asset_market',
        display_name = '株取引実験',
        num_demo_participants=3,
        app_sequence=['asset_market']
    ),
    dict(
        name = 'single_market_S1',
        display_name = '一財の市場取引実験セッション1',
        num_demo_participants = 20,
        app_sequence=['single_market_S1']
    ),
    dict(
        name = 'single_market_S2',
        display_name = '一財の市場取引実験セッション2',
        num_demo_participants = 20,
        app_sequence=['single_market_S2']
    ),
    dict(
        name = 'single_market_S3',
        display_name = '一財の市場取引実験セッション3',
        num_demo_participants = 20,
        app_sequence=['single_market_S3']
    ),
]
```

```
ROOMS = [
    dict(
    name='common_value_auction',
    display_name='共通価値オークション',
    participant_label_file='_rooms/common_value_auction.txt',
    use_secure_urls=False
    ),
    dict(
    name='doubleauction',
    display_name='ダブルオークション',
    participant_label_file='_rooms/double_auction.txt',
    use_secure_urls=False
    ),
    dict(
    name='asset_market',
    display_name='株取引実験',
    participant_label_file='_rooms/asset_market.txt',
    use_secure_urls=False
    ),
    dict(
    name='single_market',
    display_name='一財の市場取引実験S1',
    participant_label_file='_rooms/single_market.txt',
    use_secure_urls=False
    ),
    dict(
    name='single_market',
    display_name='一財の市場取引実験S2',
    participant_label_file='_rooms/single_market.txt',
    use_secure_urls=False
    ),
    dict(
    name='single_market',
    display_name='一財の市場取引実験S3',
    participant_label_file='_rooms/single_market.txt',
    use_secure_urls=False
    )

]
```

また、LANGUAGE_CODEなども書き換えます。
```
LANGUAGE_CODE = 'ja'

REAL_WORLD_CURRENCY_CODE = 'JPY'
REAL_WORLD_CURRENCY_DECIMAL_PLACES=0
USE_POINTS = False
```
8. ここからはローカル環境とリモート環境に分かれます。



## ローカル環境(オフライン)
1. Anaconda navigatorを起動します。
2. Enviromentsを開きbase(root)の三角▶からOpen Terminalを選択します。<br><br>
![image](https://user-images.githubusercontent.com/48300561/130908221-adcda5cf-b1a2-4c24-9b42-a93e7906fbc6.png) <br><br>
3. Terminal上でカレントディレクトリをoTree用のフォルダに保存したExpEconにします。
Terminalに ```otree devserver```と打ち込みます。

![image](https://user-images.githubusercontent.com/48300561/130909436-ad99a945-a1dc-48a8-a7b0-662e3395067e.png) 

4.上記のような文面が出てきますのでブラウザでhttp://localhost:8000/ を開きます。 

ここでもし次のような画面が出た場合は[こちら](https://github.com/leisurely-yucyou/oTree/blob/main/%E8%A3%9C%E8%B6%B3%E8%B3%87%E6%96%99/DEBUG%E3%83%A2%E3%83%BC%E3%83%89.md)を参照してください。デバッグモードが悪さをしています。  

![image](https://user-images.githubusercontent.com/48300561/134614554-3ee1f993-21e3-4a43-8198-b6ab58c6a55a.png)　　

5. 次のような画面が出てきたらokです。  
![image](https://user-images.githubusercontent.com/48300561/130909697-879943fb-dde0-41e3-8548-46f99307b56f.png)  
(ユーザー名とパスワードを求められた場合はsettings.pyで確認できます)  

6. あとは各自で色々触ってみてください。

7. 一応触り方を説明します。  
今回は株取引実験を触っていきます。  
次の画面で株取引実験をクリックします。  <br><br>
![image](https://user-images.githubusercontent.com/48300561/134615769-780b35ae-1c9d-444d-b889-c9df0b4cf8a7.png)  

すると次のような画面が表示されます。  <br><br>

![image](https://user-images.githubusercontent.com/48300561/134615820-819b37f7-d3da-4684-92c9-ff633654259d.png)  

デモプレイでは3人に設定しているのでSplit screen modeを起動します。  

![image](https://user-images.githubusercontent.com/48300561/134615900-fa32d73e-8fb8-43e6-90ce-e45952f8acd2.png)  

上のような画面が表示され、一つの画面で3人分の画面が表示されデバッグしやすいです。(デモプレイ人数が4人以上の場合は使用できません)  

あとはちゃんとゲームが動くかなどを確認しましょう。もし動かない場合はエラー文を読み、エラー文がよくわからないときはエラー文をそのまま検索にかけてみるといいかもしれません。


## リモート環境(オンライン)
oTree HubとHerokuを使った実験手順(自己流)です。

[oTree Hub](https://www.otreehub.com/)はoTreeによる実験の開発や設計，モニターができる便利なサイトです。   
登録自体はサイトに従って進めれば問題ないです。  
登録してログインすると次のような画面が現れます。  
![qiita1.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/f0924d1a-799b-068b-e927-f432b0942cf9.png)  

上から二番目の「Heroku server deployment」でHerokuに実験プログラムをdeployすることができます．これを使って実験を進めていきます。  
oTree HubをHerokuと連携させていない場合には次のような画面が出ます。  

![Qiita2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/151f8d5a-7550-1832-7be8-fe7762bd0c01.png)  

Herokuにアカウントを持っていない場合にはHerokuに登録する必要があるので[Heroku](https://dashboard.heroku.com)にアクセスして登録をします。
Herokuの登録手順は[「[初心者向け]herokuをデプロイしよう」](https://qiita.com/DogK0625/items/12178fdc3dd607088ff0)などを参考にしてください。  
クレジットカードの登録も必要なので行います。私自身これまで何度か実験を行いましたが、請求などはされず、無料の枠内で実験を行えているので金銭的な心配は必要ないです。(クレカという個人情報を渡すのが嫌な人もいるかもしれませんが…)  

Herokuの登録が終わったらoTree Hubの先ほどの画面に戻り、「Connect to Heroku」をクリックしてHerokuを連携させます。  
連携させると次のような画面に移ります。  

![Qiita5.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/ec521221-3ac2-9388-4ffd-ab8bba0052e1.png)  


初期状態ではHeroku Projectsには何もなく、Other Sitesにも何もないです。(私の画面では過去に行った実験の跡があります)  

ここでHerokuのサイトを開き、[Dashboard](https://dashboard.heroku.com/apps)にアクセスします。  
次のような画面が現れます。(otree-〇〇のようなものは表示されません。過去の実験の跡です)    

![Qiita3.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/c1c6433b-fb73-e8e4-5150-cb94b354361b.png)  

右上にあるNewからCreate new appをクリックします。  

![Qiita4.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/b8d7f5bf-6c5f-6fef-4a2d-dbc5c3d53004.png)  

上の画面が現れるので，好きなApp nameを入力してください。RegionはUSのままでいいです。  
入力できたらCreate appを押してHerokuでの設定は終わりです。  

![Qiita5.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/ec521221-3ac2-9388-4ffd-ab8bba0052e1.png)  

oTree Hubに戻ります。
先ほどのHeroku ProjectsのOther Sitesに先ほど作ったAppが追加されているのでRegisterをクリックします。  
Active SitesにAppが追加されるのでDeployをクリックします。  

![Qiita6.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/4e27b510-8bc6-d0cf-cf0e-be5b8fa0dbeb.png)  

上のような画面が現れるので、画面に書いてある通りの手順に従います。  

「1.Go to the "Configure" tab and enable Redis」  
これについてはスキップします。私は何もしていませんがそれでも実験は出来ました。  

「2.Upload your code below and wait for the the build to succeed」  
自分のoTreeのコードをアップロードしてくれとのことなので、まずコードを「.otreezip」に変換します。  
コマンドプロンプトでディレクトリにアクセスして「otree zip」と打ちます。もっと簡単に言うと普段デモで実験を動かすときに「otree devserver」をする場面で「otree zip」と打ちます。  

![Qiita7.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/5dac7583-696a-601e-f057-7aad442bcb8e.png)  

上のようなファイルができていればOKです。  
oTree Hubに戻って「ファイルを選択」から先ほどのファイルを選択しアップロードします。  
数分するとエラーを吐くか「Your build succeeded.」が表示されます。  
エラーが表示された場合は頑張ってエラーを処理してください。  
ファイルのアップロードに成功したら「Reser DB」をおしてDataBaseを初期化します。  
これらが終わると以下のような表示になると思います。  

![Qiita8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/e8b75375-0ce9-de8a-f306-14b68e1df947.png)  

「4.Open your app at https://otree-double-auction.herokuapp.com/.」  
最後にこのURLにアクセスします．URLは各App nameで異なります。  

![Qiita9.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/c63ebdda-da8b-782f-ca91-6faa4ac37a4e.png)  

見慣れた画面が表示されます。  
画面上部にあるRoomsにアクセスして以下の画面まで進みます。  

![Qiita10.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/f215101a-47f8-adf7-b5a4-609bd6e850e2.png)  

Session configから行う実験を選択し，Number of participantsに参加人数を入力してCreateを押してください。  
次のような画面が現れるのでURLを被験者に配布することで実験が行えます。  

![Qiita11.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/391748/5d61f570-7a2c-71e5-7f51-3eec8f76dda3.png)  

## 被験者ID(被験者番号)を設定する
被験者に任意のIDでoTreeにアクセスしてもらうための設定を行います。<br>

次の画面の[\_rooms]というフォルダを開きます。なければフォルダを作成します。<br><br>

![image](https://user-images.githubusercontent.com/48300561/134622985-905e1f2d-50f3-4f33-9007-e889fa75d490.png)
<br>

フォルダの中身に実験アプリの名前と同じ名前でテキストファイルを作成します。<br><br>

![image](https://user-images.githubusercontent.com/48300561/134623058-8f153056-18a7-4cfe-b5cf-6e7acd134d26.png)

テキストファイルに任意のIDを書いていきます。
<br><br>

![image](https://user-images.githubusercontent.com/48300561/134623253-028d5b14-c731-424c-b4a7-38087c71f5d9.png)
<br>

IDごとに改行します。またIDは英字でも構いません。必要に応じて変更してください。






