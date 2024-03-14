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

import numpy as np


class cuvreLineTrace:

        def __init__(self):
            
            pass
        
        def set_distance(self,param,tyusinx,tyusiny):
            #print("test_value",self.test)
            #print(self.param)
            x = float(param[0])
            y = float(param[1])
            #print(x)
            #print(self.goaly)
            #半径算出
            distance = (np.sqrt((tyusinx-x)**2 + (tyusiny-y)**2)) 
            #print("基準",self.standard)
            #print("現在",self.distance)
            #print(self.goalx,self.goaly)
            #print(x,y)
            return distance
                

def main():
    #print (1)
    cuvre = cuvreLineTrace()
    cuvre.stop()
        
if __name__ == '__main__':
    main()



