import numpy as np
import math

import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Judgement import Judge
from Sensors import TurnAngleSensor as TASensor,PositionMgmt as PMgmt

class DistanceJudge(Judge.Judge):

    mx=0.0    #X座標系　オブジェクト
    my=0.0   #Y座標系　オブジェクト
    mdir=0.0  #方位計   オブジェクト
    startpoint=0.0
    endpoint=0.0
    finishlength=0.0
    Pm = PMgmt.PositionMgmt()

    def __init__(self):
        pget = PMgmt.PositionMgmt()
        #mdir.get_value
        #mydir.get_value()
        #mx.get_value()
        #my.get_value()

        #XYから値取得
        positionXY = pget.getvalue()
        #mx,myに座標をセット
        self.mx = positionXY[0]
        self.my = positionXY[1]

        self.endpoint=self.find_end_point()

        #座標計算
    def find_end_point(self):

        #移動距離、現在の座標、走行体の向きから終了座標を求める

        #x軸方向の移動量
        x_move = math.cos(self.mdir * math.pi / 180) * self.finishlength

        #y軸方向の移動量
        y_move = math.sin(self.mdir * math.pi / 180) * self.finishlength
        endpoint=0
        return endpoint

    def update(self):
       self.mx,self.my= self.Pm.getvalue()


    def judge(self):

        #X、Y座標を取得し、その値が基準値をこえていたらtrueを返す。それ以外はfalse
        if -self.endpoint < 0:
            return True
        else :
            return False

        pass
    
    #これいらないかもしれない
    def getangle(self):
        angget = TASensor.TurnAngleSensor()

        #ジャイロから旋回角度抽出
        tmp = angget.getvalue()
        self.mdir = tmp['yaw']
    
    def set_param(self,judgevalue):
        self.finishlength=judgevalue

        pass
