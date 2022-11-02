# coding:utf-8
import os
import sys
import math
import pathlib
from cmath import cos, sin, sqrt
from math import fabs,pi
from Judgement.TurnAngleJudge import TurnAngleJudge
from Sensors.TurnAngleSensor import TurnAngleSensor
from Walker import Run2,PID
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import PositionMgmt,MotorMgmt
from section import SectionMgmt


#旋回の円の中心座標は走行中に決めるパターンと事前に指定するパターンある
#とりあえず右旋回を想定して作成

class curveLineTrace2(Run2):


    startx = 0.0  #自己位置？
    starty = 0.0  #自己位置?
    goalx = 0.0   #目標点?
    goaly = 0.0   #目標点?
    mForward = 0.0
    mTurn = 0.0
    mBias = 0.0
    angle2 = 0.0
    mPFactor = 0
    mIFactor = 0
    mDFactor = 0

    def __init__(self):
        #基準位置からの角度に変換
        #angle2 = TurnAngleSensor.getvalue()

        """#中心点求めてる？
        self.goalx = 5*cos((angle2/180)*pi) + self.sx
        self.goaly = 5*sin((angle2/180)*pi) + self.sy
        """
        self.startx,self.starty = PositionMgmt.getvalue()

        #Testrun用
        print("input_x?")
        self.goalx = float(input())
        print("input_y?")
        self.goaly = float(input())

        PID.reset_param()


    def set_param(PositionMgmt,kp,ki,kd,angleTarget,angleKp,self):

        self.mPFactor = kp
        self.mIFactor = ki
        self.mDFactor = kd


    def setBias(self,curve):
        self.mBias = curve

    def calcdistance(self):
        dis = sqrt(pow(self.startx - self.goalx,2) + pow(self.starty - self.goal,2))
        return dis



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