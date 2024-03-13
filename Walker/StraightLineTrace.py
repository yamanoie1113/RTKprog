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
from tkinter import W
import numpy as np


class StraightLineTrace():


        #test=0

        def __init__(self):
            
            pass
            # クラス変数
            #self.logfile = 'VirtualLine_log.txt'
            #GPSログの消去
            #LogMgmt.clear(self.logfile)
            #LogMgmt.write(self.logfile,"NONE_DISTANCE")

        def set_distance(self,param,slope,intercept):
            #print("test_value",self.test)
            #print("startx,y",self.startx,self.starty)
            #print("goalx,y",self.goalx,self.goaly)
            self.param = self.PM.getvalue()
            x = float(param[0])
            y = float(param[1])
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
            distance = abs(slope * (x) - (y) + intercept) / math.sqrt(slope**2 + 1)

            return distance

                

def main():
    #print (1)
    pa=[0,0,0,0]
    cuvre = StraightLineTrace()
    cuvre.stop()
        
if __name__ == '__main__':
    main()





