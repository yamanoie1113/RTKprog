# coding:utf-8
import os
import sys
import math
import pathlib
from cmath import cos, sin, sqrt
from math import fabs,pi
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Judgement.TurnAngleJudge import TurnAngleJudge
from Sensors.TurnAngleSensor import TurnAngleSensor
from Walker import Run2,PID
from Sensors import PositionMgmt,MotorMgmt
from section import SectionMgmt


#旋回の円の中心座標は走行中に決めるパターンと事前に指定するパターンある
#とりあえず右旋回を想定して作成

class TKcurveLineTrace(Run2):


    startx = 0.0  #初期位置
    starty = 0.0  #初期位置
    goalx = 0.0   #目標点?
    goaly = 0.0   #目標点?
    rx = 0.0      #円の中心点
    ry = 0.0      #円の中心点
    mForward = 0.0
    mTurn = 0.0
    mBias = 0.0

    """adv
    angle2 = 0.0
    mPFactor = 0
    mIFactor = 0
    mDFactor = 0
    """
    mdistance = 0
    dire = 0
    bias = 0

    def __init__(self,status):

        """
        p=status[0];
        mPID->setKp(status[0]);

        i=status[1];
        mPID->setKi(status[1]);

        d=status[2];
        mPID->setKd(status[2]);

        forw=status[3];
        bias=status[4];
        mdistance=status[5]; #半径の距離の維持


        #基準位置からの角度に変換
        #angle2 = TurnAngleSensor.getvalue()

        中心点求めてる？
        self.goalx = 5*cos((angle2/180)*pi) + self.sx
        self.goaly = 5*sin((angle2/180)*pi) + self.sy
        """
        self.startx,self.starty = PositionMgmt.getvalue() #走行体のxy座標取得

        #Testrun用
        print("input_x?")
        self.goalx = float(input())
        print("input_y?")
        self.goaly = float(input())
        print("input_bias?")
        self.bias = float(input())

        PID.set_target(self.mdistance)

    """adv
    def set_param(PositionMgmt,kp,ki,kd,angleTarget,angleKp,self):

        self.mPFactor = kp
        self.mIFactor = ki
        self.mDFactor = kd
    """

    """adv
    def setBias(self,curve):
        self.mBias = curve
    """

    def calcdistance(self):
        dis = sqrt(pow(self.startx - self.goalx,2) + pow(self.starty - self.goal,2))
        print("dis")
        print(dis)
        return dis


    def run(self,mMotormgmt):
        dire :float
        mMotormgmt.set_param(self.mForward,self.mTurn)

        x,y = PositionMgmt.getvalue()   #機体のx,y座標
        theta = TurnAngleSensor.getvalue()  #角度

        x = 5.0*cos(theta)+x # 車体幅の5.0は使わない
        y = 5.0*sin(theta)+y # 同上

        distance = self.calc_distance(self.goalx,self.goaly,x,y)
        dire = PID.get_operation(distance)

        #左回りの時に実行
        if 0 < self.mdistance:
            dire = dire * -1.0

        dire = self.bias + dire

    def reset_param():
        #初期化
        pass

def main():
    mrun=TKcurveLineTrace()
    mMotorMgmt=MotorMgmt.MotorMgmt()

if __name__=="__main__":
     main()