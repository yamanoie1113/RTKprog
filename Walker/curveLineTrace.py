# coding:utf-8
import os
import sys
import time
import pathlib
from Walker.PID import PID
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
from Sensors import PositionMgmt
from section import SectionRun2
from tkinter import W
from turtle import right
import numpy as np


class cuvreLineTrace:


        def set_param(a,b):
        
            PM = PositionMgmt.PositionMgmt()
            param = PM.getvalue()
            x = param[0] #座標分け
            y = param[1]
            a = x-300 #中心点X
            b = y-300 #中心点Y

            r = np.sqrt((a-x)**2 + (b-y)**2) #座標計算
            return r

        def set_run(self):

            self.mPID=PID()
            #self.mPID.reset_param()
            #self.param = list()
            #self.param = SectionRun2.set_param()
            r = 0
            a = 0 #中心点X
            b = 0 #中心点Y
            r = cuvreLineTrace.set_param(a,b)
            loca = r 
            turn = right
            c = 0
            

            while True:
                
                #self.mPID.set_target(loca)
                #self.mPID.set_Kpid(self.param[2],self.param[3],self.param[4])
                #self.mPID.set_limit()
                #self.mPID.get_operation()
                if r < loca:
                    #中心点に近づく
                    loca = 0
                    if turn == right:
                        MotorMgmt.set_param(0,10,100)
                    else:
                        MotorMgmt.set_param(0,10,-100)

                elif r > loca:
                    #中心点から離れる
                    loca = 0
                    if turn == right:
                        MotorMgmt.set_param(0,10,-100)
                    else:
                        MotorMgmt.set_param(0,10,100)

            
                r = cuvreLineTrace.set_param(a,b)
                time.sleep(0.1)
                c += 1
                if c == 300:
                    MotorMgmt.set_param(0,0,0)
                    #self.mPID.reset_param()
                    break
                print (c)
                

def main():
    print (1)
    cuvre = cuvreLineTrace()
    cuvre.set_run()
        
if __name__ == '__main__':
    main()
