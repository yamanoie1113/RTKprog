import numpy as np
import math

import sys
import pathlib


current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Judgement import Judge

from Sensors import PositionMgmt as PMgmt ,LogMgmt
#室外用インポート
#from Sensors import TurnAngleSensor as TASensor,PositionMgmt as PMgmt

class Distancetest(Judge.Judge):

    start_x=0.0    #X座標系　オブジェクト
    start_y=0.0   #Y座標系　オブジェクト
    mdir=0.0  #方位計   オブジェクト
    mlength =0.0
    finishlength = 0.0
    logfile = ""

    def __init__(self):
        self.pget = PMgmt.PositionMgmt()

        # クラス変数
        self.logfile = 'Distance_log.txt'

        #GPSログの消去
        LogMgmt.clear(self.logfile)
        LogMgmt.write(self.logfile,"NONE_DISTANCE")

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


    def judge(self,XYpos):
        x = XYpos[0]
        y = XYpos[1]

        self.getPosition()

        self.mlength = self.calc_dist(self.start_x,self.start_y,x,y)
        #誤差補正のために切り捨てているが、もっと良い方法があるかも
        self.mlength = round(self.mlength)

        #X、Y座標を取得し、その値が基準値をこえていたらtrueを返す。それ以外はfalse
        if self.mlength <= 0:
            return False
        else :
            return True

    def getPosition(self):
        positionXY = self.pget.getvalue()

        #start_x ,start_yに座標をセット
        self.start_x = positionXY[0]
        self.start_y = positionXY[1]

    """
    #現在角度の取得
    def getangle(self):
        angget = TASensor.TurnAngleSensor()

        #ジャイロから旋回角度抽出
        tmp = angget.getvalue()
        self.mdir = tmp['yaw']
    """


    def calc_dist(self,sx,sy,gx,gy):
        #LOGファイルオープン
        f = open(self.logfile, 'a')

        #与えられた４点の距離を計算する

        """
        テスト用現在地ダミー設定
        self.start_x = 0.0
        self.start_y = 0.0
        """

        #2点間の距離計算
        length = math.sqrt(( gx- sx)**2 + ( gy - sy)**2)
        #self.mlength = math.sqrt(( self.goal_x- self.start_x)**2 + ( self.goal_y - self.start_y)**2)

        #ログファイルに書き込み
        LogMgmt.write(self.logfile,length)


        print("距離return:",length)

        return length


    def calc_ang(self,x,y):

        #現在地の更新 しないといけないのかは考え中
        self.getPosition()

        #延長戦上に垂線を下した時の交点座標を設定
        ex_x = x                #目標地点のx
        ex_y = self.start_y     #開始地点のy

        #辺の長さ計算
        sidea_len = self.calc_dist(self.start_x,self.start_y,x,y)
        sideb_len = self.calc_dist(ex_x,ex_y,x,y)

        ang = math.asin(sideb_len/sidea_len)*180/math.pi
        return ang



    #目標となる値をここで設定したい(進みたい距離)
    def set_param(self,judgevalue):
        self.finishlength=judgevalue

def main():
    mdisjudge = Distancetest()

    #目標地点を設定
    goal_XY = [70764,-171735]

    TF = True
    #判定テスト
    while TF:
        TF=mdisjudge.judge(goal_XY)

    print("SUCCESS!!")

if __name__ == '__main__':
    main()
