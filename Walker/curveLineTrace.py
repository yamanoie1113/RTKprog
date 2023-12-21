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
        p = 0
        i = 0
        d = 0
        exec_count = 0
        log = LogMgmt.LogMgmt()
        x = 0
        y = 0
        error_sum = 0
        error_pre = 0

        def __init__(self):
            
            pass
        
        def set_distance(self):
            self.param = self.PM.getvalue()
            #print("test_value",self.test)
            #print(self.param)
            x = float(self.param[0])
            y = float(self.param[1])
            self.x = x
            self.y = y
            #print(x)
            #print(self.goaly)
            self.distance = (np.sqrt((self.tyusinx-x)**2 + (self.tyusiny-y)**2)) 
            print("基準",self.standard)
            print("現在",self.distance)
            #print(self.goalx,self.goaly)
            #print(x,y)

        def set_param(self):

            self.param = self.PM.getvalue()
        
        def init_state(self):
            self.cancel = 0
        
        def set_run(self,paramlist,goaly,Positionmgmt):
            
            self.sp = paramlist[0]
            self.sv = 0
            self.p = paramlist[1]
            self.i = paramlist[2]
            self.d = paramlist[3]
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
                while self.startx == 0:
                    time.sleep(0.1)
                    cuvreLineTrace.set_param(self)
                    self.startx = float(self.param[0])
                    self.starty = float(self.param[1])
                self.tyusinx = (self.startx + self.goalx)/2
                self.tyusiny = (self.starty + self.goaly)/2
                self.standard = (np.sqrt((self.tyusinx-self.goalx)**2 + (self.tyusiny-self.goaly)**2))
                self.log.set_param("curve_log")
                #print("goalx,y",self.goalx,self.goaly)
                #print("1kaime")
                self.cancel = 1
                self.exec_count += 1
            self.run()

        def run(self):
            try:
                
                cuvreLineTrace.set_distance(self)
                self.sv,self.error_sum,self.error_pre = self.mPID.PID(self.p,self.i,self.d,self.standard,self.distance,self.error_sum,self.error_pre)
                value = ["基準線:", self.standard, "現在線:", self.distance, "starty:",self.starty,"goalx:",self.goalx, "goaly:",self.goaly, "x:", self.x, "y:", self.y, "操作量", self.sv]
                self.log.write(value)
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



