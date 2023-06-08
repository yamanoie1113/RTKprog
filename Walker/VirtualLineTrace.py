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
from section import SectionRun
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
        MM = MotorMgmt.MotorMgmt()
        PM = PositionMgmt.PositionMgmt()
        param = [[0 for i in range(2)] for j in range(5)]
        #test=0

        def init(self):
            pass

        def set_distance(self,a):
            #print("test_value",self.test)
            #print(self.param)
            x = float(self.param[0])
            y = float(self.param[1])
            #print(x)
            #print(self.goaly)
            slope = (self.goaly - self.starty)/(self.goalx - self.startx)
            #print(slope)
            intercept = self.starty - slope * self.startx
            '''if slope == 0:
                x3 = x
            else:
                x3 = (y - intercept)/slope'''
            #x3 = y - self.starty - slope * (-1 * (self.startx)) / slpoe 
            distance = abs(slope * (x) - y + intercept) / math.sqrt(slope**2 + 1)
            #r = abs(slope * (x) + 1 * y) / np.sqrt(slope**2 + 1**2) #直線との最短距離
            VirtualLineTrace.set_turn(self,distance)
            #print(self.goalx,self.goaly)
            #print(x,y)
            return distance


        def set_turn(self,distance):
            '''if self.goaly > self.starty:
                if mx > gx:
                    self.turn = 'left' #左
                    
                elif mx < gx:
                    self.turn = 'right' #右
                else:
                    self.turn = 'no'
            elif self.goaly < self.starty: 
                if mx > gx:
                    self.turn = 'right' #右
                elif mx < gx:
                    self.turn = 'left' #左
                else:
                    self.turn = 'no'
            '''
            if 0 != distance:
                #distance = self.saitan - distance
                self.turn = 'right'
                if self.saitan < distance and self.save_turn == 'right':
                    self.turn = 'left'
            else:
                self.turn = 'no'
            self.save_turn = self.turn
            self.saitan = distance
            #VirtualLineTrace.set_saitan(self,distance)
        
        def set_saitan(self,distance):
            distance = self.saitan - distance
            if 0 != distance:
                if self.save_turn == self.turn:
                    self.save_turn = self.turn
                    if self.turn == 'left':
                        if self.save_saitan < distance:
                            self.turn = 'right'
                    elif self.turn == 'right':
                        if self.save_saitan < distance:
                            self.turn = 'left'
                    else:
                        self.turn = 'right'
            self.save_saitan = distance
            
            #print(self.turn)


        def set_param(self,a):
        
            PM = PositionMgmt.PositionMgmt()
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


        def set_run(self,paramlist,goaly):

            #self.mPID=PID()
            #self.mPID.reset_param()
            #self.param = list()
            #param_list = [0]*5
            #for f in range(4):
                #param_list = paramlist[f:f+1]
            #self.PM.__init__(self)
            sp = paramlist[0]
            sv = 0
            p = paramlist[1]
            i = paramlist[2]
            d = paramlist[3]
            #self.goalx = goaly[0]
            #self.goaly = goaly[1]
            #print(self.goalx)
            c = 0
            VirtualLineTrace.set_param(self,c)
            gy = float(goaly[0])
            gx = float(goaly[1])
            #print("param")
            #print(self.param)
            
            self.startx = float(self.param[0])
            self.starty = float(self.param[1])  
            self.goalx = self.startx + gx
            self.goaly = self.starty + gy
            #
            print(self.goalx,self.goaly)
            print(self.startx,self.starty)
            #ループカウンタ
            

            while True:

                distance = VirtualLineTrace.set_distance(self,c)
                #self.mPID.set_target(loca)
                #self.mPID.set_Kpid(self.param[2],self.param[3],self.param[4])
                #self.mPID.get_operation()
                #print(self.turn)
                if self.turn == 'no':
                    #print ('zennsin2')
                    self.MM.set_param(sp,sv)
                        #self.MM.set_param(1,100)
                if self.turn == 'right':
                    self.MM.set_param(sp,-10)
                    #self.MM.set_param(1,-100)
                    #print ('zennsin')
                elif self.turn == 'left':
                    #print ('cousin')
                    self.MM.set_param(sp,10)
                    #self.MM.set_param(10,100)
                    
                self.MM.run()
                c += 1
                if c == 5:
                    c = 2
                VirtualLineTrace.set_param(self,c)
                time.sleep(1)
                """c += 1
                if c == 100:
                    self.MM.set_param(0,0)
                    self.MM.run()
                    self.MM.stop()
                    #self.mPID.reset_param()
                    break
                #print (c)"""
                

        def stop(self):
            self.MM.set_param(0,0)
            self.MM.run()
            #self.MM.stop()
                

def main():
    #print (1)
    pa=[1,2,3,4]
    cuvre = VirtualLineTrace()
    cuvre.stop()
        
if __name__ == '__main__':
    main()


