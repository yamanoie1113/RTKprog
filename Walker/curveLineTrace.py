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
from section import SectionRun
from tkinter import W
import numpy as np


class cuvreLineTrace:

        MM = MotorMgmt.MotorMgmt()
        PM = PositionMgmt.PositionMgmt()
        goalx = 1000 #目標地点ｘ
        goaly = 1000 #目標地点ｙ
        startx = 0 #開始地点ｘ
        starty = 0 #開始地点ｙ
        turn = 'no'
        save_turn = 'no'
        tyusinx = 0
        tyusiny = 0
        standard = 0
        #save_saitan = 0
        MM = MotorMgmt.MotorMgmt()
        PM = PositionMgmt.PositionMgmt()
        param = [[0 for i in range(2)] for j in range(5)]
        sp = 0
        sv = 0
        cancel = 0

        def __init__(self):
            

            # クラス変数
            self.logfile = 'cuvreLine_log.txt'
            self.thread1 = threading.Thread(target =self.run)
            #GPSログの消去
            #LogMgmt.clear(self.logfile)
            #LogMgmt.write(self.logfile,"NONE_DISTANCE")
        
        def set_distance(self):
            #print("test_value",self.test)
            #print(self.param)
            x = float(self.param[0])
            y = float(self.param[1])
            #print(x)
            #print(self.goaly)
            if self.standard == 0:
                self.tyusin = (self.startx + self.goalx)/2
                self.tyusiny = (self.starty + self.goaly)/2
            self.distance = np.sqrt((self.tyusinx-x)**2 + (self.tyusiny-y)**2) 
            if self.standard == 0:
                self.standard = self.distance
            #LogMgmt.write(self.logfile,self.distance)
            #r = abs(slope * (x) + 1 * y) / np.sqrt(slope**2 + 1**2) #直線との最短距離
            cuvreLineTrace.set_turn(self,self.distance)
            #print(self.goalx,self.goaly)
            #print(x,y)
            return self.distance

        def set_turn(self,distance):
            if self.standard != distance:
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
            else:
                self.turn = 'no'
            self.save_turn = self.turn
            #VirtualLineTrace.set_saitan(self,distance)

        def set_param(self):
        
            #PM = PositionMgmt.PositionMgmt()
            self.param = self.PM.getvalue()
            #self.param[a][0] = 500
            #self.param[a][1] = 500
            #return self.param
        
        def set_run(self,paramlist,goaly):

            #self.mPID=PID()
            #self.mPID.reset_param()
            #self.param = list()
            #param_list = [0]*5
            #for f in range(4):
                #param_list = paramlist[f:f+1]
            #self.PM.__init__(self)
            self.sp = paramlist[0]
            self.sv = paramlist[1]
            p = paramlist[2]
            i = paramlist[3]
            d = paramlist[4]
            if self.sv > 0:
                self.save_turn = 'right'
            elif self.sv < 0:
                self.save_turn = 'left'
            #self.goalx = goaly[0]
            #self.goaly = goaly[1]
            #print(self.goalx)
            c = 0
            cuvreLineTrace.set_param(self)
            gy = float(goaly[0])
            gx = float(goaly[1])
            #print("param")
            #print(self.param)
            
            self.startx = float(self.param[0])
            self.starty = float(self.param[1])  
            self.goalx = gx
            self.goaly = gy
            #
            #print(self.goalx,self.goaly)
            #print(self.startx,self.starty)
            #ループカウンタ
            if self.cancel == 0:
                self.thread1.start()
                self.cancel = 1
            if self.sp == 0: 
                self.cancel = 2
                self.thread1.join()
                self.cancel = 0


        def run(self):
            try:
                c = 0
                while True:

                    cuvreLineTrace.set_distance(self)
                    #self.mPID.set_target(loca)
                    #self.mPID.set_Kpid(self.param[2],self.param[3],self.param[4])
                    #self.mPID.get_operation()
                    #print(self.turn)
                    if self.turn == 'no':
                        #print ('zennsin2')
                        self.MM.set_param(self.sp,self.sv)
                            #self.MM.set_param(1,100)
                    if self.turn == 'right':
                        self.sv = self.sv + 30
                        if self.sv > 100:
                            self.sv = 100
                        self.MM.set_param(self.sp,self.sv)
                        #self.MM.set_param(1,-100)
                        #print ('zennsin')
                    elif self.turn == 'left':
                        #print ('cousin')
                        self.sv = self.sv - 30
                        if self.sv < -100:
                            self.sv = -100
                        self.MM.set_param(self.sp,self.sv)
                        #self.MM.set_param(10,100)
                    
                    self.MM.run()
                    if self.cancel == 2:
                        break
                    c += 1
                    if c == 5:
                        c = 2
                    #VirtualLineTrace.set_param(self)
                    time.sleep(0.1)
                    """c += 1
                    if c == 100:
                        self.MM.set_param(0,0)
                        self.MM.run()
                        self.MM.stop()
                        #self.mPID.reset_param()
                        break
                    #print (c)"""
            except KeyboardInterrupt:
                print("complet")


        def stop(self):
            self.MM.set_param(0,0)
            self.MM.run()
            self.MM.stop()
                

def main():
    #print (1)
    cuvre = cuvreLineTrace()
    cuvre.set_run(1,100,0,0,0)
        
if __name__ == '__main__':
    main()



