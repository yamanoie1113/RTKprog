# coding:utf-8
import os
import sys
import time
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
from Sensors import PositionMgmt
from tkinter import W
from turtle import right
import numpy as np


class cuvreLineTrace:


        def set_param(a,b):
        
            PM = PositionMgmt.PositionMgmt()
            param = PM.getvalue()
            param = [5,7]
            x = param[0] #座標分け
            y = param[1]
            a = x-1 #中心点X
            b = y-1 #中心点Y
            r = np.sqrt((a-x)**2 + (b-y)**2) #座標計算
            return r

        def set_run(self):

            
            r = 0
            a = 0 #中心点X
            b = 0 #中心点Y
            r = cuvreLineTrace.set_param(a,b)
            loca = r 
            turn = right
            c = 0
            

            while True:
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

            
                cuvreLineTrace.set_param(a,b)
                time.sleep(0.1)
                c += 1
                if c == 600:
                    MotorMgmt.set_param(0,0,0)
                    break
                print (c)
                

def main():
    print (1)
    cuvre = cuvreLineTrace()
    cuvre.set_run()
        
if __name__ == '__main__':
    main()
