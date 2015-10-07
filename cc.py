# -*- coding: UTF-8 -*-
#上記コメントを記述することで，日本語コメントが可能。
#文字コードは“shift-jis”の他に，“utf-8”,“euc-jp”，“cp932”などなど。
#使用するエディタによって設定を変える。
 
#numpyをインポート
from numpy import *
#matplotlibのインターフェースであるpylabをインポート
import pylab as plt
 
#“linspace(開始値，終了値，分割数)”で，線形数列を作成。
x = linspace(-pi, pi, 100)
 
#数列をsinの引数に入れると，sin(x)の数列が生成される。
y = sin(x)
 
#とりあえずplot。
plt.plot(x,y)
 
#plotした関数を表示する。
plt.show()
