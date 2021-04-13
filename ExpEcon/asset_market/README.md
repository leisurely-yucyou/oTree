# 株取引ゲーム(資産市場のバブル実験)
## 2020年度実施状況
- 3人1グループを20グループで実施
- Zoomを用いてグループごとにブレイクアウトルームに割り振り
- 1ラウンド3分
- 10ラウンド

## プログラム変更可能箇所
- グループ数
- 1ラウンドの時間
- ラウンド数

## グループ数の変更方法
「_rooms」というフォルダに入っている「asset_market.txt」の中身を任意のグループ数まで書き足す。  
「asset_market.txt」の中身は以下のようになっている。  
![スクリーンショット 2021-04-13 162758](https://user-images.githubusercontent.com/48300561/114513534-3e952300-9c75-11eb-98d0-50ed5df8dd0a.png)  


## 1ラウンドの時間の変更方法
「[asset_market/pages.py](https://github.com/leisurely-yucyou/oTree/blob/741324aabb1a5a15bf4b1bdc8fe4fa233b9edcd6/ExpEcon/asset_market/pages.py)」というファイルの16行目
```
timeout_seconds = 
```
を書き換える。  
![スクリーンショット 2021-04-13 163300](https://user-images.githubusercontent.com/48300561/114514145-f1658100-9c75-11eb-8f16-aa85ee3715dc.png)

## ラウンド数の変更方法
「[asset_market/models.py](https://github.com/leisurely-yucyou/oTree/blob/741324aabb1a5a15bf4b1bdc8fe4fa233b9edcd6/ExpEcon/asset_market/models.py)」というファイルの18行目
```
num_rounds = 
```
を書き換える。  
![スクリーンショット 2021-04-13 163901](https://user-images.githubusercontent.com/48300561/114514942-ccbdd900-9c76-11eb-89ab-1a8bd5ab044f.png)
