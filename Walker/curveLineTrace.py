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


class cuvreLineTrace:


        def set_param(a,b):
        
            #PM = PositionMgmt.PositionMgmt()
            #para = PM.getvalue()
            para = [500,500]
            x = para[0] #座標分け
            y = para[1]
            #a = x-300 #中心点X
            #b = y-300 #中心点Y

            r = np.sqrt((a-x)**2 + (b-y)**2) #座標計算
            return r

        def set_run(self,sp,sv,p,i,d):

            #self.mPID=PID()
            #self.mPID.reset_param()
            #self.param = list()
            MM = MotorMgmt.MotorMgmt()
            r = 0 #現在半径
            loca = 0 #目標半径
            a = 300 #中心点X
            b = 300 #中心点Y
            r = cuvreLineTrace.set_param(a,b)
            loca = r
            turn = right #旋回半径
            c = 0#ループカウンタ
            

            while True:
                
                #self.mPID.set_target(loca)
                #self.mPID.set_Kpid(self.param[2],self.param[3],self.param[4])
                #self.mPID.get_operation()

                
                if r < loca:
                    #中心点に近づく
                    if turn == right:
                        MM.set_param(sp,sv)
                        #MM.set_param(1,100)
                        #print ('zennsin')
                    else:
                        #print ('cousin')
                        MM.set_param(sp,sv)
                        #MM.set_param(10,-100)

                elif r > loca:
                    #中心点から離れる
                    if turn == right:
                        #print ('zennsin2')
                        MM.set_param(sp,sv)
                        #MM.set_param(1,-100)
                    else:
                        #MM.set_param(10,100)
                        MM.set_param(sp,sv)
                        #print ('cousin2')
                else:
                    if turn == right:
                        #MM.set_param(1,100)
                        MM.set_param(sp,sv)
                        #print ('zennsin')
                    else:
                        #print ('cousin')
                        MM.set_param(sp,sv)
                        #MM.set_param(10,-100)

                MM.run()
                r = cuvreLineTrace.set_param(a,b)
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
    cuvre = cuvreLineTrace()
    cuvre.set_run(1,100,0,0,0)
        
if __name__ == '__main__':
    main()

