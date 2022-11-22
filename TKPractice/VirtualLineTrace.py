import sys
import pathlib
import math

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Walker import Run,Run2
from Sensors import PositionMgmt#,TurnAngleSensor as TASensor
#from section import SectionRun

#直線仮想ライントレースお試し実装　使えるかどうかわからん

class VirtualLineTrace(Run2.Run2):
    x = 0.0
    y = 0.0
    p = 0.0
    i = 0.0
    d = 0.0

    #initの引数が配列かどうかわからん。たぶん配列？
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        #こいつらは受け取った値を設定するはず？
        self.p = 0.0
        self.i = 0.0
        self.d = 0.0

    def set_param(self,x,y,p,i,d):
        self.x = x
        self.y = y
        self.p = p
        self.i = i
        self.d = d

    def run(self):
        x,y = PositionMgmt.PositionMgmt.getvalue() #現在地xy取得
        th = 320 #dummy!
        #th = TASensor.TurnAngleSensor.getvalue()   #現在角度取得
        x = math.cos(th) + x
        y = math.sin(th) + y
        print("run_x,y")
        print(x,y)

    def reset_param(self):
        self.__init__()

    def calc_distance(nowX,nowY,x1,y1,x2,y2):
        dis = (y2 - y1)*nowX - (x2)


def main():
    tcls = VirtualLineTrace()
    print(vars(tcls))
    tcls.run()

    """ run以外のメソッド確認
    tcls.set_param(1,2,3,4,5)
    print(vars(tcls))
    tcls.reset_param()
    print(vars(tcls))
    """

if __name__=="__main__":
    main()