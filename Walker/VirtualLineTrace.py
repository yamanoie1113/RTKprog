# coding:utf-8
import os
import sys
import time
import pathlib
import math
import time
#from Walker.PID import PID
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
from Sensors import PositionMgmt
from Sensors import LogMgmt
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
        slope = 0
        intercept = 0
        #save_saitan = 0
        MM = MotorMgmt.MotorMgmt()
        PM = None
        mPID = PID2.PID()
        param = [[0 for i in range(2)] for j in range(5)]
        sp = 0
        sv = 0
        cancel = 0
        p = 0
        i = 0
        d = 0
        bunp = 0
        log = LogMgmt.LogMgmt()
        error_sum = 0
        error_pre = 0
        x = 0
        y = 0
        nx = 0
        ny = 0


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
            #print("startx,y",self.startx,self.starty)
            #print("goalx,y",self.goalx,self.goaly)
            self.param = self.PM.getvalue()
            x = float(self.param[0])
            y = float(self.param[1])
            self.x = x
            self.y = y
            #print("x",x,"y",y)
            
            #print(x,y)
            #print(self.goaly)
            #print('distance')            
            '''if slope == 0:
                x3 = x
            else:
                x3 = (y - intercept)/slope
            '''           
            #x3 = y - self.starty - slope * (-1 * (self.startx)) / slpoe 
            distance = abs(self.slope * (x) - (y) + self.intercept) / math.sqrt(self.slope**2 + 1)
            #print(distance)
            #LogMgmt.write(self.logfile,distance)
            #nx = (y-intercept)/slope
            #最短座標
            #'''
            t = (-1*self.slope * x - (-1) * y - self.intercept) / (self.slope * self.slope + (-1) * (-1))
            nx = x + self.slope * t
            ny = y + (-1) * t
            self.nx = nx
            self.ny = ny
            #'''
            #tyokusen = np.sqrt((self.goalx - x)**2+(self.goaly - y)**2)
            #print(tyokusen)
            #r = abs(slope * (x) + 1 * y) / np.sqrt(slope**2 + 1**2) #直線との最短距離
            VirtualLineTrace.set_turn(self,distance,x,y,nx,ny)
            #print(self.goalx,self.goaly)
            #print(x,y)

        def set_bunp(self):
            if self.startx <= self.goalx and self.starty <= self.goaly:
                self.bunp = 1
            elif self.startx >= self.goalx and self.starty <= self.goaly:
                self.bunp = 2
            elif self.startx >= self.goalx and self.starty >= self.goaly:
                self.bunp = 3
            elif self.startx <= self.goalx and self.starty >= self.goaly:
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
            #print("kite")
            self.param = self.PM.getvalue()
        
        def init_state(self):
            self.cancel = 0

        def set_run(self,paramlist,goaly,Positionmgmt):
            #print("dete")
            self.PM=Positionmgmt
            self.sp = paramlist[0]
            self.sv = 0
            self.p = paramlist[1]
            self.i = paramlist[2]
            self.d = paramlist[3]
            g = paramlist[4]
            sv = 0
            if g == "straight_right":
                g = -1
                sv = 100 * g
            if g == "straight_left":
                g = 1
                sv = 100 * g
            if g == "straight_leftt":
                g = 1
                sv = 100 * g
            VirtualLineTrace.set_param(self)
            #print("param")
            #print(self.param)            
            #print(self.goalx,self.goaly)
            #print(self.startx,self.starty)
            #ループカウンタ
            if self.cancel == 0:
                if sv != 0:   
                    self.MM.set_param(self.sp,sv)
                    self.MM.run()
                    time.sleep(0.9)
                self.goalx = float(goaly[0])
                self.goaly = float(goaly[1])
                self.startx = float(self.param[0])
                self.starty = float(self.param[1])
                while self.startx == 0:
                    time.sleep(0.1)
                    VirtualLineTrace.set_param(self)
                    self.startx = float(self.param[0])
                    self.starty = float(self.param[1])
                value = ["直線との距離:", "startx:", "starty:","goalx:", "goaly:", "x:", "y:", "操作量","sp"]    
                #value = ["操作量"]
                self.log.set_param(value,"virtual_log")
                VirtualLineTrace.set_bunp(self)
                self.slope = (self.goaly - self.starty)/(self.goalx - self.startx)
                self.intercept = self.starty - self.slope * self.startx
                self.cancel = 1                
            self.run()            


        def run(self):
            try:
                print(0)
                VirtualLineTrace.set_distance(self)
                self.sv,self.error_sum,self.error_pre = self.mPID.PID(self.p,self.i,self.d,0,self.save_saitan,self.error_sum,self.error_pre)
                value = [self.save_saitan,self.startx,self.starty,self.goalx, self.goaly, self.x, self.y, self.sv,self.sp]
                #value = [self.sv]
                self.log.write(value)
                #self.sv = self.sv * -1
                #self.MM.set_param(self.sp,self.sv)
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
    pa=[0,0,0,0]
    cuvre = VirtualLineTrace()
    cuvre.stop()
        
if __name__ == '__main__':
    main()





