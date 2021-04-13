# 2財の取引ゲーム(ケニア実験)

## 2020年度実施状況
- 1グループ2~3人を20グループ
- グループ1-10をタイプA、グループ11-20をタイプB
- 1ラウンド6分
- 5ラウンド

## プログラム変更可能箇所
- 1ラウンドの時間
- ラウンド数

## 1ラウンドの時間の変更
「[double_auction/pages.py](https://github.com/leisurely-yucyou/oTree/blob/e8a0f0958fd704063ba16bb7d7452753f63433ac/ExpEcon/double_auction/pages.py)」の23行目  
```
timeout_seconds = 
```
を書き換える。  
![スクリーンショット 2021-04-13 173246](https://user-images.githubusercontent.com/48300561/114522370-4d340800-9c7e-11eb-842b-654029fd5a05.png)

## ラウンド数の変更
「[double_auction/models.py](https://github.com/leisurely-yucyou/oTree/blob/e8a0f0958fd704063ba16bb7d7452753f63433ac/ExpEcon/double_auction/models.py)」の18行目  
```
num_rounds = 
```
を書き換える。  
![スクリーンショット 2021-04-13 173433](https://user-images.githubusercontent.com/48300561/114522703-908e7680-9c7e-11eb-9dc8-d0405995d9bb.png)
