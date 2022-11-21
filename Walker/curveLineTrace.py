# coding:utf-8
import os
import sys
import time
import pathlib
from tkinter import W
from turtle import right
import numpy as np
from math import fabs
from Walker.Run import Run
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import PositionMgmt



class cuvreLineTrace(Run):

     
    startx = 0
    starty = 0
    goalx = 0
    goaly = 0


    def set_param(PositionMgmt,a,b):
        
        
        PositionMgmt.getvalue(param)
        param = [1,2]
        x = param[0] #座標分け
        y = param[1]
        a = x-1 #中心点X
        b = y-1 #中心点Y
        r = np.sqrt((a-x)**2 + (b-y)**2) #座標計算
        return r

    def set_run(self,):

        
        r = 0
        a = 0 #中心点X
        b = 0 #中心点Y
        r = cuvreLineTrace.set_param(0,a,b)
        loca = r 
        turn = right

        while True:
            if r < loca:
                #中心点に近づく
                loca = 0
                if turn == right:
                    MotorMgmt.set_param(30,100,0)
                else:
                    MotorMgmt.set_param(30,-100,0)

            elif r > loca:
                #中心点から離れる
                loca = 0
                if turn == right:
                    MotorMgmt.set_param(30,-100,0)
                else:
                    MotorMgmt.set_param(30,100,0)

            
            cuvreLineTrace.set_param(loca)
            time.sleep(0.1)