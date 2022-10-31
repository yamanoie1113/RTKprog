# coding:utf-8
import os
import sys
import math
import pathlib
from cmath import cos, sin, sqrt
from math import fabs
from Walker.Run2 import Run2
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import PositionMgmt
from section import SectionMgmt
from Sensors import MotorMgmt

#旋回の円の中心座標は走行中に決めるパターンと事前に指定するパターンある

class curveLineTrace2(Run2):


    startx = 0.0  #自己位置？
    starty = 0.0  #自己位置
    goalx = 0.0   #目標点
    goaly = 0.0   #目標点
    mForward = 0.0
    mTurn = 0.0

    def __init__(self):
        self.set_param()

    def set_param(PositionMgmt,self):
        self.startx,self.starty = PositionMgmt.getvalue()



    def run(self,mMotormgmt):

        mMotormgmt.set_param(self.mForward,self.mTurn)

        """
        SectionMgmt
        z = (d-b)/(c-a)
        x=(y+z*a-b)/z
        startz = z
        position = True
        while position == False:
            VirtualLineTrace.set_param(param)
            gz = (d-parab)/(c-paraa)
            raz = (z - gz)/(1 + z*gz)
            math.degrees(math.atan(raz))
        """

    def reset_param():
        #初期化
        pass

def main():
    mrun=curveLineTrace2()
    mMotorMgmt=MotorMgmt.MotorMgmt()

if __name__=="__main__":
     main()