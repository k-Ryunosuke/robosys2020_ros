# robosys2020_ros
## 概要
*Tomと接待じゃんけんをするプログラムです。r, s, p(r:rock, s:scissors, p:paper)のうちから1つの文字をキーボードから入力すると、それに負けるような結果が別の端末に出力されます。r, s, p以外の文字を入力した場合、入力画面にr, s, pを入力してくださいという指示が出力され、別端末の結果にはxが出力されます。*
## 動作環境
- Raspberry Pi 4 Model B
- Ubuntu 20.04
- ROS noetic
## 環境構築
*このパッケージをROSのsrcフォルダ下にインストールする。*
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/momokohara/robosys2020_ros.git
$ cd ..
$ catkin_make
```
## 実行方法
1. <端末1>でroscoreを立ち上げる。
```
$ roscore
```
2. <端末2>でプログラムを立ち上げる。
```
$ rosrun robosys2020_ros rock_scissors_paper.py
```
3. <端末3>でpublishされたデータを取り出せるようにする。
```
$ rostopic echo /result
```
4. <端末2>でキーボードから r, s, p(Tomを困らせたいときはそれ以外の文字)を入力する。
5. <端末3>で、出力された結果を確認する。
## デモ動画
- Youtubeのデモ動画は[こちら](https://youtu.be/bias6SwiM2o)
## 参考サイト
*ソースコードは[こちら](https://demura.net/education/lecture/16773.html)のサイトを参考にしています。*
