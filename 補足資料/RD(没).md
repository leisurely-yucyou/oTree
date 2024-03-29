# oTreeによる実験手順とその準備
oTreeで実験を行う方法はいくつかありますが、僕のやり方を書いています。  
明治大学の後藤先生をはじめ、oTreeに関する日本語のサイトも増えてきているのでそちらを参照するのもいいと思います。
 
## 事前に準備すること
 - Anacondaのインストール
 - テキストエディタのインストール

※Anacondaのインストールがまだの場合は「[Anaconda で Python 環境をインストールする](https://qiita.com/t2y/items/2a3eb58103e85d8064b6)」を参考に準備してください。  
※テキストエディタはあった方が後の作業が楽になります。「[Visual Studio Code (Windows版) のインストール](https://qiita.com/psychoroid/items/7d85ae6bade4a67aedb1)」などを参考にしてください。VSCodeでなくても大丈夫です。

## 各実験の説明書
 - [株取引ゲーム](https://github.com/leisurely-yucyou/oTree/blob/387375d9ed0ff76a20a3084f6b0e8c1e991cdd6d/ExpEcon/asset_market/README.md)
 - [共通価値オークション](https://github.com/leisurely-yucyou/oTree/blob/bb430fc990c11bf4c360d76b5cc89f02e3333791/ExpEcon/common_value_auction_5/README.md)
 - [2財の取引ゲーム(ケニア実験)](https://github.com/leisurely-yucyou/oTree/blob/7fc9f36fa3a2712103af242a463eacc9e5f41b39/ExpEcon/double_auction/README.md)
 - [1財の取引ゲーム(発泡酒実験)](https://github.com/leisurely-yucyou/oTree/blob/66c40518fbbea483db70eb7dc0a79391a81a3aae/ExpEcon/single_market_S1/README.md)

## 実験手順
オンライン実験を行う方法には
- HerokuとoTree hub
- AWS
の2通りがあります。  
僕は前者でやっています。僕のやり方はQiitaにまとめてありますのでそちらを参照してください。  
「[oTree Hubを用いたオンライン実験](https://qiita.com/leisurely/private/ab1b31b2e8084ce3fb6a)」
