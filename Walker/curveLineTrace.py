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


class cuvreLineTrace:


        def set_param(a,b):
        
            PM = PositionMgmt.PositionMgmt()
            para = PM.getvalue()
            #para = [500,500]
            x = para[0] #座標分け
            y = para[1]
            #a = x-200 #中心点X
            #b = y-300 #中心点Y

            r = np.sqrt((a-x)**2 + (b-y)**2) #座標計算
            print('x:',x,'y:',y) 
            return r
        
        def fast_param(a,b):
        
            PM = PositionMgmt.PositionMgmt()
            para = PM.getvalue()
            #para = [500,500]
            x = para[0] #座標分け
            y = para[1]
            a = x+300 #中心点X
            b = y #中心点Y

            r = np.sqrt((a-x)**2 + (b-y)**2) #座標計算
            print('x:',x,'y:',y) 
            return r,a,b

        def set_run(self,sp,sv,p,i,d):

            #self.mPID=PID()
            #self.mPID.reset_param()
            #self.param = list()
            MM = MotorMgmt.MotorMgmt()
            r = 0 #現在半径
            loca = 0 #目標半径
            a = 0#中心点X
            b = 0 #中心点Y
            #para = [500,500]
            r,a,b = cuvreLineTrace.fast_param(a,b)
            loca = r
            turn = 'right' #旋回半径
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
                
                if c < 10:
                    MM.set_param(30,100)
                elif r < loca:
                    #中心点に近づく
                    if turn == 'right':
                        #MM.set_param(sp,sv)
                        MM.set_param(30,100)
                        print ('zennsin')
                    else:
                        print ('cousin')
                        #MM.set_param(sp,sv)
                        MM.set_param(30,-100)
                elif r > loca:
                    #中心点から離れる
                    if turn == 'right':
                        print ('zennsin2')
                        #MM.set_param(sp,sv)
                        MM.set_param(30,-100)
                    else:
                        MM.set_param(30,100)
                        #MM.set_param(sp,sv)
                        print ('cousin2')
                else:
                    if turn == 'right':
                        MM.set_param(30,80)
                        #MM.set_param(sp,sv)
                        print ('zennsin3')
                    else:
                        #print ('cousin')
                        MM.set_param(sp,sv)
                        MM.set_param(30,-100)

                MM.run()
                r = cuvreLineTrace.set_param(a,b)
                time.sleep(0.1)
                c += 1
                if c == 50:
                    
                    #f.close()
                    #self.mPID.reset_param()
                    break
                #print (c)


        def stop():
            MM = MotorMgmt.MotorMgmt()
            MM.set_param(0,0)
            MM.run()
            MM.stop()
                

def main():
    #print (1)
    cuvre = cuvreLineTrace()
    cuvre.set_run(1,100,0,0,0)
        
if __name__ == '__main__':
    main()


