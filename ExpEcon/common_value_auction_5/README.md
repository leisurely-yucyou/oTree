# 共通価値オークション(5人版)
10人版は[こちら](https://github.com/leisurely-yucyou/oTree/blob/7196b542dae3eb2c0f8d80d328af7ea34a66e6e4/ExpEcon/common_value_auction_10/README.md)
## 2020年度実施状況
- グループ分けは無し(個人プレイ)
- 1ラウンドの時間制限なし
- 2ラウンド

## プログラム変更可能箇所
- プレイヤー数
- 1ラウンドの時間制限
- ラウンド数

## プレイヤー数の変更方法
「[_rooms/common_value_auction.txt](https://github.com/leisurely-yucyou/oTree/blob/30c0dfe703244f2694e9cb763693b99edca8a758/ExpEcon/_rooms/common_value_auction.txt)」というファイルの中身を任意の人数まで書き足す。  
ファイルの中身は以下のようになっている。  
![スクリーンショット 2021-04-13 165319](https://user-images.githubusercontent.com/48300561/114516916-ce889c00-9c78-11eb-885f-f173485ef30e.png)

## 1ラウンドの時間制限
時間制限を付けることも可能だが、プレイヤーが時間制限内に価格を入力しなかった場合の処理をプログラムしなければいけない。  
必要であればご連絡ください。  

## ラウンド数の変更
「[common_value_auction_5/models.py](https://github.com/leisurely-yucyou/oTree/blob/30c0dfe703244f2694e9cb763693b99edca8a758/ExpEcon/common_value_auction_5/models.py)」というファイルの24行目  
```
num_rounds = 
```
を書き換える。  
![スクリーンショット 2021-04-13 170124](https://user-images.githubusercontent.com/48300561/114518057-eca2cc00-9c79-11eb-8490-de58fdf5bfba.png)


