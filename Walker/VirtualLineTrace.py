# coding:utf-8
import os
import sys
import time
import pathlib
#from Walker.PID import PID
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
from Sensors import PositionMgmt
from section import SectionRun
from tkinter import W
from turtle import right
import numpy as np


class VirtualLineTrace:

        goalx = 1000 #目標地点ｘ
        goaly = 1000 #目標地点ｙ
        startx = 0 #開始地点ｘ
        starty = 0 #開始地点ｙ
        turn = 'no'



        def set_distance(self,para):
            x = para[0]
            y = para[1]
            x2 = (self.goaly - self.starty)/(self.goalx - self.startx)
            x3 = y - self.starty - x2 * (-self.startx) / x2 
            VirtualLineTrace.set_turn(x3,x)

            r = abs(x2 * (x) + 1 * y) / np.sqrt(x2**2 + 1**2) #直線との最短距離            
            return r


        def set_turn(self,mx,gx):
            
            if self.goaly > self.starty:
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


        def set_param(self):
        
            PM = PositionMgmt.PositionMgmt()
            #para = PM.getvalue()
            param = [500,500]
            return param


        def set_run(self,sp,sv,p,i,d):

            #self.mPID=PID()
            #self.mPID.reset_param()
            #self.param = list()
            MM = MotorMgmt.MotorMgmt()
            param = VirtualLineTrace.set_param()
            self.startx = param[0]
            self.starty = param[1]  
            c = 0#ループカウンタ
            

            while True:
                
                #self.mPID.set_target(loca)
                #self.mPID.set_Kpid(self.param[2],self.param[3],self.param[4])
                #self.mPID.get_operation()

                if self.turn == 'no':
                     #print ('zennsin2')
                        MM.set_param(sp,sv)
                        #MM.set_param(1,100)
                elif r < 0:
                    #中心点に近づく
                    if self.turn == 'right':
                        MM.set_param(sp,sv)
                        #MM.set_param(1,-100)
                        #print ('zennsin')
                    elif self.turn == 'left':
                        #print ('cousin')
                        MM.set_param(sp,sv)
                        #MM.set_param(10,100)
                elif r > 0:
                    #中心点から離れる
                    if self.turn == 'right':
                        #print ('zennsin2')
                        MM.set_param(sp,sv)
                        #MM.set_param(1,-100)
                    elif self.turn == 'left':
                        #MM.set_param(10,100)
                        MM.set_param(sp,sv)
                        #print ('cousin2')

                    
                MM.run()
                param =VirtualLineTrace.set_param()
                r = VirtualLineTrace.set_distance(param)
                time.sleep(0.1)
                c += 1
                if c == 100:
                    MM.set_param(0,0)
                    MM.run()
                    MM.stop()
                    #self.mPID.reset_param()
                    break
                #print (c)
                

def main():
    #print (1)
    cuvre = VirtualLineTrace()
    cuvre.set_run(1,100,0,0,0)
        
if __name__ == '__main__':
    main()

