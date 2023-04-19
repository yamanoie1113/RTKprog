import numpy as np
import math

import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Judgement import Judge

from Sensors import PositionMgmt as PMgmt,TurnAngleSensor as TASensor

class PointJudge(Judge.Judge):

    start_x=0.0    #X開始
    start_y=0.0   #Y開始
    goal_x = 0.0  #x終了
    goal_y = 0.0  #y終了

    mxlength = 0.0  #x座標の距離
    mylength = 0.0  #y座標の距離

    def __init__(self):
        self.pget = PMgmt.PositionMgmt()

    def judge(self,x,y):

        #座標の更新
        self.getPosition()

        #x座標の判定
        if self.mxlength <= 0:
            #y座標の判定

            if self.mylength <= 0:
                return True
            else :
                return False

        else :
             return False


    def set_param():

        pass

    def getPosition(self):
        positionXY = self.pget.getvalue()

        #クラス変数に座標をセット
        self.start_x = positionXY[0]
        self.start_y = positionXY[1]


    def calc_dist(self,end_x,end_y):

        #現在地の設定
        self.getPosition()

        """
        テスト用現在地ダミー設定
        self.start_x = 0.0
        self.start_y = 0.0
        """

        #目標値が一つずつの場合　必要なかったら消す
        self.goal_x = end_x
        self.goal_y = end_y

        #ｘ座標の直線距離
        self.mxlength = (self.goal_x - self.start_x)

        #y座標の直線距離
        self.mylength = (self.goal_y - self.start_y)


    #目標となる値をここで設定したい(進みたい距離)
    def set_param(self,judgevalue):
        self.finishlength=judgevalue


    def calc_ang(self,x,y):

        #延長戦上に垂線を下した時の交点座標を設定
        ex_x = x                #目標地点のx
        ex_y = self.start_y     #開始地点のy




#テスト
def main():
    pass

if __name__ == '__init__' :
    main()