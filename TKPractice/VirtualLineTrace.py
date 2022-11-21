import sys
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#from Walker import Run これいらない？
from section import SectionRun

#直線仮想ライントレースお試し実装　使えるかどうかわからん

class VirtualLineTrace():
    x = 0.0
    y = 0.0
    p = 0.0
    i = 0.0
    d = 0.0

    #initの引数が配列かどうかわからん。たぶん配列？
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        #こいつらは受け取った値を設定する
        self.p = 0.0
        self.i = 0.0
        self.d = 0.0
