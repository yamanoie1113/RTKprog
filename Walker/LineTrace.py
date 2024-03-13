# coding:utf-8
import os
import sys
import time
import pathlib
import math
import threading
#from Walker.PID import PID
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
from Sensors import PositionMgmt
from Sensors import LogMgmt
from Walker import PID2
from Walker import StraightLineTrace
from Walker import curveLineTrace
from section import SectionRun

from tkinter import W
import numpy as np


class LineTrace:

        MM = MotorMgmt.MotorMgmt()
        PM = None
        goalx = 1000 #目標地点ｘ
        goaly = 1000 #目標地点ｙ
        startx = 0 #開始地点ｘ
        starty = 0 #開始地点ｙ
        turn = 'no'
        save_turn = 'no'
        tyusinx = 0
        tyusiny = 0
        standard = 0
        distance = 0 
        save_saitan = 0
        mPID = PID2.PID()
        straight = StraightLineTrace.StraightLineTrace()
        curve = curveLineTrace.cuvreLineTrace()
        param = [[0 for i in range(2)] for j in range(5)]
        sp = 0
        sv = 0
        cancel = 0
        p = 0
        i = 0
        d = 0
        exec_count = 0
        log = LogMgmt.LogMgmt()
        x = 0
        y = 0

        def __init__(self):
            
            pass
        

        def set_param(self):

            self.param = self.PM.getvalue()
        
        def init_state(self):
            self.cancel = 0
        
        def set_run(self,paramlist,goaly,Positionmgmt):
            
            self.PM=Positionmgmt
            self.sp = paramlist[0]
            self.sv = 0
            pid = paramlist[1]
            self.p = pid[0]
            self.i = pid[1]
            self.d = pid[2]
            goaly = paramlist[2]
            self.select = paramlist[3]

            sv = 0
            if self.select == "straight_right":
                sv = -100
            if self.select == "straightt_left":
                sv = 100
            if self.select == "curve_right":
                sv = -70
            if self.select == "curve_left":
                sv = 70
            #print(self.goalx)
            #print("curve_goal")
            #print(goaly)
            
            #print("param")
            #print(self.param)
            # 
            #print(self.goalx,self.goaly)
            #print(self.startx,self.starty)
            #ループカウンタ           
            if self.cancel == 0:
                self.MM.set_param(30,sv)
                self.MM.run()
                self.PM=Positionmgmt
                #初期座標取得
                LineTrace.set_param(self)
                self.goalx = float(goaly[0])
                self.goaly = float(goaly[1])
                self.startx = float(self.param[0])
                self.starty = float(self.param[1])
                #初期ゲイン
                self.MM.set_param(30,sv)
                self.MM.run()
                while self.startx == 0:
                    time.sleep(0.1)
                    LineTrace.set_param(self)
                    self.startx = float(self.param[0])
                    self.starty = float(self.param[1])
                self.tyusinx = (self.startx + self.goalx)/2
                self.tyusiny = (self.starty + self.goaly)/2
                #print("goalx,y",self.goalx,self.goaly)
                #print("1kaime")
                #初期半径
                self.standard = (np.sqrt((self.tyusinx-self.goalx)**2 + (self.tyusiny-self.goaly)**2))
                self.slope = (self.goaly - self.starty)/(self.goalx - self.startx)
                self.intercept = self.starty - self.slope * self.startx
                self.cancel = 1
                self.exec_count += 1
            self.run()

        def run(self):
            try:
                #半径の取得
                self.param = self.PM.getvalue()
                if self.select == "straight_right" or self.select == "straight_left":
                    distance = self.straight.set_distance(self.param,self.slope,self.intercept)
                    #PIDを使う
                    self.sv= self.mPID.PID(self.p,self.i,self.d,0,distance)
                if self.select == "curve_right" or self.select == "curve_left":
                    distance = self.curve.set_distance(self.param,self.tyusinx,self.starty)
                    #PIDを使う
                    self.sv= self.mPID.PID(self.p,self.i,self.d,self.standard,distance)
                
                #if self.exec_count % 2 == 0:
                    #self.sv *= -1
                
                self.MM.set_param(self.sp,self.sv)
                self.MM.run()
                
            except KeyboardInterrupt:
                print("complet")


        def stop(self):
            self.MM.set_param(0,0)
            self.MM.run()
            #self.MM.stop()
                

def main():
    #print (1)
    cuvre = cuvreLineTrace()
    cuvre.stop()
        
if __name__ == '__main__':
    main()



