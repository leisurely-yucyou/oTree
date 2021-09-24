## コマンドプロンプトでカレントディレクトリを変更する方法

Windowsでの説明となります。(Mac, Linuxの方は申し訳ありませんが各自検索してください)    

画面左下にあるホームメニューで「コマンドプロンプト」もしくは「cmd」と検索します。  

![image](https://user-images.githubusercontent.com/48300561/134612427-ca38563a-47ed-48c8-89bf-1e6184d9a733.png)  

一番上に出てくるコマンドプロンプトを起動します。  

![cmd](https://user-images.githubusercontent.com/48300561/134612634-da5499e6-c20e-4e18-9b7e-4b4859f39d79.png)

起動すると上記のような画面が表示されます。  

次にカレントディレクトリをoTree用のフォルダに設定します。  

![cmd2](https://user-images.githubusercontent.com/48300561/134612843-8cae2ad0-42c9-4a52-951c-c43594ad5d47.png)    

コマンドプロンプト上で  
```
cd ~~~
```
のように打ち込みます。波線の部分はoTree用のフォルダのPATHです。またドライブをまたいで変更する場合は```cd```を```cd/d```と打ち込んでください。  

これでカレントディレクトリを変更できました。  

PATHが分からない場合はそのフォルダを開き、次の画像のように確認することができます。  

![image](https://user-images.githubusercontent.com/48300561/134613094-e816a60e-b316-42b5-945e-184708b5dd56.png)



