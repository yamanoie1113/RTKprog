import numpy as np
import math

import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Judgement import Judge

from Sensors import PositionMgmt as PMgmt,TurnAngleSensor as TASensor

#室外用インポート
#from Sensors import TurnAngleSensor as TASensor,PositionMgmt as PMgmt

class DistanceJudge(Judge.Judge):

    start_x=0.0    #X座標系　オブジェクト
    start_y=0.0   #Y座標系　オブジェクト
    mdir=0.0  #方位計   オブジェクト
    mlength =0.0
    finishlength = 0.0

    def __init__(self):
        self.pget = PMgmt.PositionMgmt()
        #mdir.get_value
        #mydir.get_value()
        #mx.get_value()
        #my.get_value()

        #XY値取得
        #self.getPosition()

        #self.endpoint=self.find_end_point()

    """
    #座標計算 これいらんかも
    def find_end_point(self):
        print("find_endpoint")
        #移動距離、現在の座標、走行体の向きから終了座標を求める

        #x軸方向の移動量
        x_move = math.cos(self.mdir * math.pi / 180) * self.finishlength

        #y軸方向の移動量
        y_move = math.sin(self.mdir * math.pi / 180) * self.finishlength

        #到着地点のxy座標を計算（あってるかわからん）
        goal_x = self.mx + x_move
        goal_y = self.my + y_move


        self.endpoint=0
        print("done.endpoint:",end="")
        print(self.endpoint)
    """


    def judge(self):
        self.calc_dist()
        
        #あと、計算周りを自分たちの仕様に直す
        #X、Y座標を取得し、その値が基準値をこえていたらtrueを返す。それ以外はfalse
        if self.mlength <= 0:
            return True
        else :
            return False

    def getPosition(self):
        positionXY = self.pget.getvalue()

        #mx ,myに座標をセット
        self.start_x = positionXY[0]
        self.start_y = positionXY[1]


    #これいらないかもしれない.到達地点を求めるために必要だが、今回はGPSがあるため
    def getangle(self):
        angget = TASensor.TurnAngleSensor()

        #ジャイロから旋回角度抽出
        tmp = angget.getvalue()
        self.mdir = tmp['yaw']

    def calc_dist(self,end_x,end_y):

        #現在地ダミー設定
        self.start_x = 0.0
        self.start_y = 0.0

        #現在地の設定
        self.getPosition()



        #目標値が一つずつの場合　必要なかったら消す
        self.goal_x = end_x
        self.goal_y = end_y

        #目標値が配列の場合　必要なかったら消す
        #self.goal_x = endpoint[0]
        #self.goal_y = endpoint[1]

        #2点間の距離計算
        self.mlength = math.sqrt(( self.goal_x- self.start_x)**2 + ( self.goal_y - self.start_y)**2)
        self.mlength = round(self.mlength)
        print("距離",self.mlength)


    #目標となる値をここで設定したい(進みたい距離)
    def set_param(self,judgevalue):
        self.finishlength=judgevalue

def main():
    mdisjudge = DistanceJudge()

    goal_x = 0.0
    goal_y = 0.0

    mdisjudge.calc_dist(goal_x,goal_y)

if __name__ == '__main__':
    main()
