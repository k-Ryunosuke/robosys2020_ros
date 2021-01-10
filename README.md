# robosys2020_ros
## 概要
*接待じゃんけんをするプログラムです。r, s, c(r:rock, s:scissors, p:paper)のうちから1つの文字をキーボードから入力すると、それに負けるような結果がpublishで画面に出力されます。r, s, c以外の文字を入力した場合、入力画面にr, s, cを入力してくださいという指示が出力され、結果にはxがpublishされます。*
## 動作環境
- Raspberry Pi 4 Model B
- Ubuntu 20.04
- ROS noetic
## 環境構築
1. このパッケージをROSのsrcフォルダ下にインストールする。
```
$ cd ~/catkin_ws/src
$ git clone 
