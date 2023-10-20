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
from Walker import PID2
from section import SectionRun
from tkinter import W
import numpy as np


class cuvreLineTrace:

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
        param = [[0 for i in range(2)] for j in range(5)]
        sp = 0
        sv = 0
        cancel = 0
        error_sum = 0
        error_pre = 0
        p = 0
        i = 0
        d = 0
        exec_count = 0

        def __init__(self):
            
            pass
            # クラス変数
            #self.logfile = 'cuvreLine_log.txt'
            #GPSログの消去
            #LogMgmt.clear(self.logfile)
            #LogMgmt.write(self.logfile,"NONE_DISTANCE")
        
        def set_first(self):
            #print("test_value",self.test)
            #print(self.param)
            #x = float(self.param[0])
            #y = float(self.param[1])
            #print("x,y",x,y)
            #print(self.goaly)            
            self.tyusinx = (self.startx + self.goalx)/2
            self.tyusiny = (self.starty + self.goaly)/2
            print(self.tyusinx,"  ",self.tyusiny)
            self.standard = (np.sqrt((self.tyusinx-self.goalx)**2 + (self.tyusiny-self.goaly)**2))
            #print("standard",self.standard)
            #LogMgmt.write(self.logfile,self.distance)
            #r = abs(slope * (x) + 1 * y) / np.sqrt(slope**2 + 1**2) #直線との最短距離
            #print(self.goalx,self.goaly)
            #print(x,y)
        
        def set_distance(self):
            self.param = self.PM.getvalue()
            #print("test_value",self.test)
            #print(self.param)
            x = float(self.param[0])
            y = float(self.param[1])
            #print(x)
            #print(self.goaly)
            self.distance = (np.sqrt((self.tyusinx-x)**2 + (self.tyusiny-y)**2)) 
            #print("基準",self.standard)
            #print("現在",self.distance)
            #LogMgmt.write(self.logfile,self.distance)
            #r = abs(slope * (x) + 1 * y) / np.sqrt(slope**2 + 1**2) #直線との最短距離
            #cuvreLineTrace.set_turn(self,self.distance)
            #print(self.goalx,self.goaly)
            #print(x,y)
            #return self.distance

        def set_turn(self,distance):
            #distance = self.saitan - distance
            if self.save_turn == 'right':
                if self.standard < distance :
                    self.turn = 'right'
                else:
                    self.turn = 'left'
            elif self.save_turn == 'left':
                if self.standard < distance :
                    self.turn = 'left'
                else:
                    self.turn = 'right'
            self.save_turn = self.turn
            #VirtualLineTrace.set_saitan(self,distance)

        def set_param(self):
        
            #PM = PositionMgmt.PositionMgmt()
            self.param = self.PM.getvalue()
            #self.param[a][0] = 500
            #self.param[a][1] = 500
            #return self.param

        def PID(self,kp,ki,kd,theta_goal,theta_current,error_sum,error_pre):
            
            #pidが小さい時
            '''
            if theta_current < 1 and theta_current > 0:
                theta_current = theta_current *100
            elif theta_current > -1 and theta_current < 0:
                theta_current = theta_current *10
            '''
            theta_current = theta_current*10
            error = theta_goal - (theta_current)# 偏差（error）を計算            
            error_sum += error*0.01 # 偏差の総和（積分）を計算
            #ki = 0       		
            error_diff = (error-error_pre)/0.5 # PI制御からの追加：1時刻前の偏差と現在の偏差の差分（微分）を計算    		
            m = (kp * error) + (ki * error_sum) + (kd * error_diff) # 操作量を計算             
            m = m
            #print("m",m)
            m = math.floor(m)
            if m >= 100:
                m = 90
            elif m <= -100:
                m = -90
            #print("m",m)
            return m, error_sum, error
        
        def init_state(self):
            self.cancel = 0
        
        def set_run(self,paramlist,goaly,Positionmgmt):
            #self.mPID=PID()
            #self.mPID.reset_param()
            #self.param = list()
            #param_list = [0]*5
            #for f in range(4):
                #param_list = paramlist[f:f+1]
            #self.PM.__init__(self)
            
            self.sp = paramlist[0]
            self.sv = 0
            self.p = paramlist[1]
            self.i = paramlist[2]
            self.d = paramlist[3]
            #self.goalx = goaly[0]
            #self.goaly = goaly[1]
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
                self.PM=Positionmgmt
                cuvreLineTrace.set_param(self)
                self.goalx = float(goaly[0])
                self.goaly = float(goaly[1])
                self.startx = float(self.param[0])
                self.starty = float(self.param[1])
                cuvreLineTrace.set_first(self)
                print("goalx,y",self.goalx,self.goaly)
                print("1kaime")
                self.cancel = 1
                self.exec_count += 1
            self.run()

        def run(self):
            try:
                
                cuvreLineTrace.set_distance(self)
                self.sv,self.error_sum,self.error_pre = self.mPID.PID(self.p,self.i,self.d,self.standard,self.distance,self.error_sum,self.error_pre)
                if self.exec_count % 2 == 0:
                    self.sv *= -1
                
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



