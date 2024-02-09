import numpy as np
import math

import sys
import pathlib,time,threading
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Judgement import Judge

from Sensors import LogMgmt,PositionMgmt as PMgmt,TurnAngleSensor as TASensor

#室外用インポート
#from Sensors import TurnAngleSensor as TASensor,PositionMgmt as PMgmt

class DistanceJudge(Judge.Judge):

    start_x=0.0    #X座標系　オブジェクト
    start_y=0.0   #Y座標系　オブジェクト
    mdir=0.0  #方位計   オブジェクト
    mlength =0.0
    finishlength = 0.0
    logfile = ''

    def __init__(self):
        pass
        #self.pget = PMgmt.PositionMgmt()
        #self.pget.PosMgmt_init()
        #self.PositionMgmt_init()
        
                

        # クラス変数
        #self.logfile = 'Distance_log.txt'
        #self.judgelog = 'DisJudge_log.txt'

        #GPSログの消去
        
        #LogMgmt.write(self.logfile,"NONE_DISTANCE")

        
        #LogMgmt.write(self.judgelog,"NONE_JUDGED")

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
       

    def judge(self,XYpos,PMgmt):
        #print(XYpos)
        start_time = time.perf_counter()
        
        x = XYpos[0]
        y = XYpos[1]

        #受け取ったインスタンスで現在地を取得
        positionXY=PMgmt.getvalue()

        #スライス
        self.start_x = positionXY[0]
        self.start_y = positionXY[1]

        self.mlength = self.calc_dist(self.start_x,self.start_y,x,y)
        #誤差補正のために切り捨てているが、もっと良い方法があるかも
        #self.mlength = round(self.mlength)
        print("to_goal:",self.mlength)
        
        #print("dis",self.mlength)

        #X、Y座標を取得し、その値が基準値をこえていたらtrueを返す。それ以外はfalse
        if self.mlength <= 2.3:
            #LogMgmt.write(slf.judgelog,"reached")
            #print("AAAAAAAAA")
            #print(self.mlength)
            return False
        else :
            #LogMgmt.write(self.judgelog,"UN_reached")
            #print("UN_REACHED")
            #print(self.mlength)
            return True
        
        stop = time.perf_counter() - start_time
        print("DIS_JUDGE_time",stop)

    #本番では使わない
    def getPosition(self):
        positionXY = self.pget.getvalue()

        #start_x ,start_yに座標をセット
        self.start_x = positionXY[0]
        self.start_y = positionXY[1]
        #print(self.start_x,self.start_y)


    #現在角度の取得
    def getangle(self):
        angget = TASensor.TurnAngleSensor()

        #ジャイロから旋回角度抽出
        tmp = angget.getvalue()
        self.mdir = tmp['yaw']


    def calc_dist(self,sx,sy,gx,gy):

        #与えられた４点の距離を計算する

        """
        テスト用現在地ダミー設定
        self.start_x = 0.0
        self.start_y = 0.0
        """

        #2点間の距離計算
        length = ( gx- sx)**2 + ( gy - sy)**2
        #self.mlength = math.sqrt(( self.goal_x- self.start_x)**2 + ( self.goal_y - self.start_y)**2)

        #ログファイルに書き込み
        #LogMgmt.write(self.logfile,length)

        #print("距離return:",length)

        return length


    #旋回角度の計算
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
    
    def get_Goal(self):
        
        goal_x = self.pget.Point[0][0]
        goal_y = self.pget.Point[0][1]
        
        return goal_x,goal_y


    #目標となる値をここで設定したい(進みたい距離)
    def set_param(self,judgevalue):
        self.finishlength=judgevalue

def main():
    goal_XY = [[0,0],[0,0]]
    mdisjudge = DistanceJudge()
    
    #goal_x,goal_y = mdisjudge.get_Goal()
    goal_XY[0] = 1.0
    goal_XY[1] = 1.0

    Flag = True
    #判定テスト
    while Flag:
        Flag = mdisjudge.judge(goal_XY)
        #print(Flag)
        
    print("aaa")
if __name__ == '__main__':
    main()
