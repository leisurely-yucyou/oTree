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
1. まず、画像の右上のCodeボタン(緑色のボタン)をクリックしDwonload ZipからZipファイルをダウンロードします。  
![image](https://user-images.githubusercontent.com/48300561/130906017-a06c47d4-ee15-4b82-b94a-7fdf239df275.png)

2. デスクトップなどにoTree用のフォルダを準備しておきます。
3. コマンドプロンプト等でカレントディレクトリを先ほど作ったoTree用のフォルダに設定する
4. ``` otree startproject otreetest```をコマンドプロンプト等で打ち込む(otreetestの部分は任意のワードに変えてください)
5. 4番でoTree用フォルダ内にプロジェクトが出来たのでカレントディレクトリをそこに変更する
7. 先ほどダウンロードしたZipファイルをoTree用フォルダに展開します。
8. ここからはローカル環境とリモート環境に分かれます。

ステップ3がわからない場合は[こちら](https://github.com/leisurely-yucyou/oTree/blob/main/%E8%A3%9C%E8%B6%B3%E8%B3%87%E6%96%99/cmd%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6.md)

## ローカル環境(オフライン)
5. Anaconda navigatorを起動します。
6. Enviromentsを開きbase(root)の三角▶からOpen Terminalを選択します。 ![image](https://user-images.githubusercontent.com/48300561/130908221-adcda5cf-b1a2-4c24-9b42-a93e7906fbc6.png)
7. Terminal上でカレントディレクトリをoTree用のフォルダに保存したExpEconにします。
8. Terminalに ```otree devserver```と打ち込みます。  
![image](https://user-images.githubusercontent.com/48300561/130909436-ad99a945-a1dc-48a8-a7b0-662e3395067e.png)  
上記のような文面が出てきますのでブラウザでhttp://localhost:8000/ を開きます。
9. 次のような画面が出てきたらokです。  ![image](https://user-images.githubusercontent.com/48300561/130909697-879943fb-dde0-41e3-8548-46f99307b56f.png)
  (ユーザー名とパスワードを求められた場合、初期設定はユーザー名「admin」、パスワード「economics2020」になっています。)
10. あとは各自で色々触ってみてください。

## リモート環境(オンライン)
Qiitaの私の[記事](https://qiita.com/leisurely/private/ab1b31b2e8084ce3fb6a)を参照してください。
