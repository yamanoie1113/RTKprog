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
        saitan = 0
        #save_saitan = 0
        MM = MotorMgmt.MotorMgmt()
        PM = PositionMgmt.PositionMgmt()
        param = [[0 for i in range(2)] for j in range(5)]
        sp = 0
        sv = 0
        cancel = 0

        def __init__(self):
            

            # クラス変数
            self.logfile = 'VirtualLine_log.txt'
            self.thread1 = threading.Thread(target =self.run)
            #GPSログの消去
            #LogMgmt.clear(self.logfile)
            #LogMgmt.write(self.logfile,"NONE_DISTANCE")
        
        def set_distance(self,a):
            #print("test_value",self.test)
            #print(self.param)
            x = float(self.param[0])
            y = float(self.param[1])
            #print(x)
            #print(self.goaly)
            print('distance')
            slope = (self.goaly - self.starty)/(self.goalx - self.startx)
            #print(slope)
            intercept = self.starty - slope * self.startx
            '''if slope == 0:
                x3 = x
            else:
                x3 = (y - intercept)/slope'''
            #x3 = y - self.starty - slope * (-1 * (self.startx)) / slpoe 
            self.distance = abs(slope * (x) - y + intercept) / math.sqrt(slope**2 + 1)
            self.distance = self.distance/2
            #LogMgmt.write(self.logfile,self.distance)
            print('distance2')
            #r = abs(slope * (x) + 1 * y) / np.sqrt(slope**2 + 1**2) #直線との最短距離
            VirtualLineTrace.set_turn(self,self.distance)
            #print(self.goalx,self.goaly)
            #print(x,y)
            return self.distance


        def set_param(self,a,b):
        
            #PM = PositionMgmt.PositionMgmt()
            para = self.PM.getvalue()
            #para = [500,500]
            x = para[0] #座標分け
            y = para[1]
            #a = x-200 #中心点X
            #b = y-300 #中心点Y

            r = np.sqrt((a-x)**2 + (b-y)**2) #座標計算
            print('x:',x,'y:',y) 
            return r
        
        def fast_param(self,a,b):
        
            #PM = PositionMgmt.PositionMgmt()
            #para = self.PM.getvalue()
            para = [500,500]
            x = para[0] #座標分け
            y = para[1]
            a = x+300 #中心点X
            b = y #中心点Y

            r = np.sqrt((a-x)**2 + (b-y)**2) #座標計算
            print('x:',x,'y:',y) 
            return r,a,b

        def right_run(self,paramlist):

            #self.mPID=PID()
            #self.mPID.reset_param()
            #self.param = list()
            #MM = MotorMgmt.MotorMgmt()
            param_list = [0]*5
            for f in range(4):
                param_list = paramlist[f:f+1]
            
            sp = param_list[0]
            sv = param_list[1]
            p = param_list[2]
            i = param_list[3]
            d = param_list[4]
            r = 0 #現在半径
            loca = 0 #目標半径
            a = 0#中心点X
            b = 0 #中心点Y
            #para = [500,500]
            r,a,b = cuvreLineTrace.fast_param(a,b)
            loca = r
            c = 0#ループカウンタ
            #f = open('log.txt', 'w')
            

            while True:
                
                #self.mPID.set_target(loca)
                #self.mPID.set_Kpid(self.param[2],self.param[3],self.param[4])
                #self.mPID.get_operation()

                #if c < 20:
                    #para = [700,700]
                #elif c > 40:
                    #para  = [300,300]
                #else:    
                    #para = [500,500]
                #f.write(r,a,b \n)
                print('loca',loca,'r:',r,'a:',a,'b:',b)
                
                #if c < 10:
                    #MM.set_param(30,100)
                if r < loca:
                    #中心点に近づく
                    #MM.set_param(sp,sv)
                    self.MM.set_param(30,100)
                    print ('zennsin')

                elif r > loca:
                    #中心点から離れる
                    print ('zennsin2')
                    #MM.set_param(sp,sv)
                    self.MM.set_param(30,-100)

                else:
                    self.MM.set_param(30,100)
                    #MM.set_param(sp,sv)
                    print ('zennsin3')


                self.MM.run()
                r = cuvreLineTrace.set_param(a,b)
                time.sleep(0.1)
                c += 1
                
                #if c == 50:
                    #cuvreLineTrace.stop()
                    #f.close()
                    #self.mPID.reset_param()
                    #break
                #print (c)


        def left_run(self,paramlist):
            #self.mPID=PID()
            #self.mPID.reset_param()
            #self.param = list()
            #MM = MotorMgmt.MotorMgmt()
            print(paramlist)
            sp = paramlist[0]
            sv = paramlist[1]
            p = paramlist[2]
            i = paramlist[3]
            d = paramlist[4]
            print('sp',sp,sv,p,i,d)
            r = 0 #現在半径
            loca = 0 #目標半径
            a = 0#中心点X
            b = 0 #中心点Y
            #para = [500,500]
            #r,a,b = cuvreLineTrace.fast_param(a,b)
            loca = r
            c = 0#ループカウンタ
            #f = open('log.txt', 'w')
            
            #while True:
                
                #self.mPID.set_target(loca)
                #self.mPID.set_Kpid(self.param[2],self.param[3],self.param[4])
                #self.mPID.get_operation()

                #if c < 20:
                    #para = [700,700]
                #elif c > 40:
                    #para  = [300,300]
                #else:    
                    #para = [500,500]
                #f.write(r,a,b \n)
            print('sp',sp,sv,p,i,d)
            print('loca',loca,'r:',r,'a:',a,'b:',b)
                #if r < loca:
                    #中心点に近づく
            print ('cousin')
            self.MM.set_param(sp,sv)
                    #self.MM.set_param(30,-100)
                #elif r > loca:
                    #self.MM.set_param(30,100)
                    #MM.set_param(sp,sv)
                    #print ('cousin2')
                #else:
                    #print ('cousin')
                    #self.MM.set_param(sp,sv)
                    #self.MM.set_param(30,-100)

            self.MM.run()
                #r = cuvreLineTrace.set_param(a,b)
            time.sleep(0.1)
            #c += 1
                
                #if c == 50:
                    #cuvreLineTrace.stop()
                    #f.close()
                    #self.mPID.reset_param()
                    #break
                #print (c)

        
        def run(self,paramlist):
            param_list = [0]*5
            for f in range(4):
                param_list = paramlist[f:f+1]
            
            sp = param_list[0]
            sv = param_list[1]
            p = param_list[2]
            i = param_list[3]
            d = param_list[4]
            c = 0#ループカウンタ
            while True:      
                self.MM.set_param(sp,sv)
                self.MM.run()
                time.sleep(0.1)
                #if c == 50:
                    #cuvreLineTrace.stop()
                    #f.close()
                    #self.mPID.reset_param()
                    #break


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



