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
import numpy as np


class VirtualLineTrace():

        goalx = 1000 #目標地点ｘ
        goaly = 1000 #目標地点ｙ
        startx = 0 #開始地点ｘ
        starty = 0 #開始地点ｙ
        turn = 'no'
        MM = MotorMgmt.MotorMgmt()
        #test=0

        def init(self):
            pass

        def set_distance(self,para):
            #print("test_value",self.test)
            print(para)
            x = para[0]
            y = para[1]
            #print(x)
            #print(self.goaly)
            x2 = (self.goaly - self.starty)/(self.goalx - self.startx)
            x3 = y - self.starty - x2 * (-1 * (self.startx)) / x2 
            VirtualLineTrace.set_turn(self,x3,x)

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


        def fast_param(self,a,b):
        
            #PM = PositionMgmt.PositionMgmt()
            #para = self.PM.getvalue()
            para = [500,500]
            x = para[0] #座標分け
            y = para[1]
            a = x+300 #中心点X
            b = y #中心点Y

            r = np.sqrt((a-x)**2 + (b-y)**2) #座標計算
            #print('x:',x,'y:',y) 
            return r,a,b


        def set_run(self,paramlist):

            #self.mPID=PID()
            #self.mPID.reset_param()
            #self.param = list()
            #param_list = [0]*5
            #for f in range(4):
                #param_list = paramlist[f:f+1]
            sp = paramlist[0]
            sv = 0
            p = paramlist[1]
            i = paramlist[2]
            d = paramlist[3]
            #print(self.goalx)
            param = VirtualLineTrace.set_param(self)
            self.startx = param[0]
            self.starty = param[1]  
            c = 0
            #print(sp,sv)
            #ループカウンタ
            

            while True:
                
                #self.mPID.set_target(loca)
                #self.mPID.set_Kpid(self.param[2],self.param[3],self.param[4])
                #self.mPID.get_operation()

                if self.turn == 'no':
                     #print ('zennsin2')
                    self.MM.set_param(sp,sv)
                        #self.MM.set_param(1,100)
                elif r < 0:
                    #中心点に近づく
                    if self.turn == 'right':
                        self.MM.set_param(sp,sv)
                        #self.MM.set_param(1,-100)
                        #print ('zennsin')
                    elif self.turn == 'left':
                        #print ('cousin')
                        self.MM.set_param(sp,sv)
                        #self.MM.set_param(10,100)
                elif r > 0:
                    #中心点から離れる
                    if self.turn == 'right':
                        #print ('zennsin2')
                        self.MM.set_param(sp,sv)
                        #self.MM.set_param(1,-100)
                    elif self.turn == 'left':
                        #self.MM.set_param(10,100)
                        self.MM.set_param(sp,sv)
                        #print ('cousin2')

                    
                self.MM.run()
                param =VirtualLineTrace.set_param(self)
                r = VirtualLineTrace.set_distance(self,param)
                time.sleep(0.1)
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
            self.MM.stop()
                

def main():
    #print (1)
    pa=[1,2,3,4]
    cuvre = VirtualLineTrace()
    cuvre.set_run(pa)
        
if __name__ == '__main__':
    main()


