# coding:utf-8
import os
import sys
import time
import pathlib
import math
#from Walker.PID import PID
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
from Sensors import PositionMgmt
from Walker import PID2
from tkinter import W
import numpy as np


class VirtualLineTrace():

        goalx = 1000 #目標地点ｘ
        goaly = 1000 #目標地点ｙ
        startx = 0 #開始地点ｘ
        starty = 0 #開始地点ｙ
        turn = 'no'
        save_turn = 'no'
        saitan = 0
        save_saitan = 0
        #save_saitan = 0
        MM = MotorMgmt.MotorMgmt()
        PM = PositionMgmt.PositionMgmt()
        mPID = PID2.PID()
        param = [[0 for i in range(2)] for j in range(5)]
        sp = 0
        sv = 0
        cancel = 0
        p = 0
        i = 0
        d = 0
        error_sum = 0
        error_pre = 0
        bunp = 0


        #test=0

        def __init__(self):
            
            pass
            # クラス変数
            #self.logfile = 'VirtualLine_log.txt'
            #GPSログの消去
            #LogMgmt.clear(self.logfile)
            #LogMgmt.write(self.logfile,"NONE_DISTANCE")

        def set_distance(self):
            #print("test_value",self.test)
            #print(self.param)
            self.param = self.PM.getvalue()
            x = float(self.param[0])
            y = float(self.param[1])
            #print(x)
            #print(self.goaly)
            #print('distance')
            slope = (self.goaly - self.starty)/(self.goalx - self.startx)
            #print(slope)
            intercept = self.starty - slope * self.startx
            '''if slope == 0:
                x3 = x
            else:
                x3 = (y - intercept)/slope
            '''
            #x3 = y - self.starty - slope * (-1 * (self.startx)) / slpoe 
            distance = abs(slope * (x) - (y) + intercept) / math.sqrt(slope**2 + 1)
            #LogMgmt.write(self.logfile,distance)
            #nx = (y-intercept)/slope
            #最短座標
            #'''
            t = (-1*slope * x - (-1) * y - intercept) / (slope * slope + (-1) * (-1))
            nx = x + slope * t
            ny = y + (-1) * t
            #'''
            #tyokusen = np.sqrt((self.goalx - x)**2+(self.goaly - y)**2)
            #print(tyokusen)
            #r = abs(slope * (x) + 1 * y) / np.sqrt(slope**2 + 1**2) #直線との最短距離
            VirtualLineTrace.set_turn(self,distance,x,y,nx,ny)
            #print(self.goalx,self.goaly)
            #print(x,y)

        def set_bunp(self):
            if self.startx <= self.goalx and self.starty <= self.startx:
                self.bunp = 1
            elif self.startx >= self.goalx and self.starty <= self.startx:
                self.bunp = 2
            elif self.startx >= self.goalx and self.starty >= self.startx:
                self.bunp = 3
            elif self.startx <= self.goalx and self.starty >= self.startx:
                self.bunp = 4

        def set_turn(self,distance,x,y,nx,ny):
            #ONOFF回路の
            ''' 
            if 0 <= distance:
                #distance = self.saitan - distance
                self.turn = 'right'
                self.save_saitan = distance
                if self.saitan < distance and self.save_turn == 'right':
                    self.turn = 'left'
                    self.save_saitan = self.save_saitan * (-1)
            else:
                self.turn = 'no'
            self.save_turn = self.turn
            self.saitan = distance
            #VirtualLineTrace.set_saitan(self,distance)
            '''
            if 0 <= distance:
                #print('distance',distance)
                #print('self.save_saitan',self.save_saitan)
                self.save_saitan = distance
                if self.bunp ==1 or self.bunp ==2:
                    if nx <= x:
                        self.turn = 'left'
                        self.save_saitan = self.save_saitan * (-1)
                    else:
                        self.turn = 'right'
                if self.bunp ==3 or self.bunp ==4:
                    if nx <= x:
                        self.turn = 'right'
                    else:
                        self.turn = 'left'
                        self.save_saitan = self.save_saitan * (-1)
            #print(self.turn)
            #'''

        def set_param(self):
        
            #PM = PositionMgmt.PositionMgmt()
            self.param = self.PM.getvalue()
            #self.param[a][0] = 500
            #self.param[a][1] = 500
            #return self.param


        def fast_param(self,a,b,c):
        
            #PM = PositionMgmt.PositionMgmt()
            #para = self.PM.getvalue(self)
            self.param[c][0] = 500
            self.param[c][1] = 500
            x = self.param[c][0] #座標分け
            y = self.param[c][1]
            a = x+300 #中心点X
            b = y #中心点Y

            r = np.sqrt((a-x)**2 + (b-y)**2) #座標計算
            #print('x:',x,'y:',y) 
            return r,a,b

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
            error_diff = (error-error_pre)/0.01 # PI制御からの追加：1時刻前の偏差と現在の偏差の差分（微分）を計算    		
            m = (kp * error) + (ki * error_sum) + (kd * error_diff) # 操作量を計算             
            m = m/12
            #print("m",m)
            m = math.floor(m)
            if m >= 100:
                m = 90
            elif m <= -100:
                m = -90
            #print("m",m)
            return m, error_sum, error

        def set_run(self,paramlist,goaly):
            print("dete")
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
            VirtualLineTrace.set_param(self)
            gy = float(goaly[0])
            gx = float(goaly[1])
            #print("param")
            #print(self.param)
            
            self.startx = float(self.param[0])
            self.starty = float(self.param[1])  
            self.goalx = gx
            self.goaly = gy
            VirtualLineTrace.set_bunp(self)
            #
            #print(self.goalx,self.goaly)
            #print(self.startx,self.starty)
            #ループカウンタ
            if self.cancel == 0:
                self.run()
                self.cancel = 1
            if self.sp == 0: 
                self.stop()


        def run(self):
            try:
                while True:
                    start = time.perf_counter()
                    VirtualLineTrace.set_distance(self)
                    #self.mPID.set_Kpid(self.param[2],self.param[3],self.param[4])
                    self.sv,self.error_sum,self.error_pre = self.mPID.PID(self.p,self.i,self.d,0,self.save_saitan,self.error_sum,self.error_pre)
                    #self.sv,self.error_sum,self.error_pre = VirtualLineTrace.PID(self.p,self.i,self.d,0,self.save_saitan,self.error_sum,self.error_pre)
                    #print(self.turn)
                    if self.turn == 'no':
                        #print ('zennsin2')
                        self.MM.set_param(self.sp,self.sv)
                        #self.MM.set_param(self.sp,50)
                    if self.turn == 'right':
                        self.MM.set_param(self.sp,self.sv)
                        #self.MM.set_param(self.sp,-50)
                        #print ('zennsin')
                    elif self.turn == 'left':
                        #print ('cousin')
                        self.MM.set_param(self.sp,self.sv)
                        #self.MM.set_param(10,100)
                    
                    self.MM.run()
                    if self.cancel == 2:
                        break
                    #c += 1
                    #if c == 5:
                    #    c = 2
                    #time.sleep(0.1)
                    #print("tyokusen",time.perf_counter() - start)
            except KeyboardInterrupt:
                print("complet")


        def stop(self):
            self.MM.set_param(0,0)
            self.MM.run()
            #self.MM.stop()
                

def main():
    #print (1)
    pa=[0,0,0,0]
    cuvre = VirtualLineTrace()
    cuvre.stop()
        
if __name__ == '__main__':
    main()





