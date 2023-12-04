<<<<<<< HEAD
# coding:utf-8
=======

# coding: utf-8 
#from multiprocessing import Process
#from concurrent.futures import ProcessPoolExecutor
#import multiprocessing
>>>>>>> baba1c9ae2601aab786c769d6047e9d82c2adedc
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import SectionMgmt
import threading

#import Timerset
#import rpipwmtest
import time

# メインプロセスで動かす関数

class Mgmt:
    
    sectionMgmt=SectionMgmt.SectionMgmt()
    judge=False

    def __init__(self):
    
        print("プログラム開始")
        self.sectionMgmt.preparation()#走行準備
        
    def preparation(self):
        
        #コース判別
        while True:
            
            print('<Corse select> 1:Normal_Course 2:REIWA_Course 3:Circuit_Course')
            self.course_select = input('>> ')
                
            if self.course_select in ['1','2','3']:
                print('OK')
                break
            
            else:
                print('Try agein')
        
        
        self.sectionMgmt.preparation(self.course_select)#走行準備
        
    def start(self):
        
        print('メインプロセスStart')

        state=True #ステートの設定

        start_program = time.perf_counter()
        while state:
            
            start_time = time.perf_counter()
            

            run_time=self.timejudge(start_program)
            if self.course_select != 3:
                
                if (run_time>=180): #.................走行時間の設定
                    state=False
                    break
                
                self.sectionMgmt.Run()

                #秒数の計算
                stop = time.perf_counter() - start_time
                if stop <= 0.5:
                    
                    
                    stop = 0.5-stop
                    time.sleep(stop)
                
                else:
                    
                    pass
                    #print("counter",time.perf_counter()-start_time)
            else:
                
                
                self.judge=self.sectionMgmt.circuit_run()
                if self.judge==True:
                    break
                
                stop = time.perf_counter() - start_time
                if stop <= 0.5:
                    
                    #print("秒数",time.perf_counter()-start_time)
                    stop = 0.5-stop
                    time.sleep(stop)
                
                else:
                    
                    pass
                
        print("タイム: ",time.perf_counter()-start_time)  
                
        #self.sectionMgmt.end()
        print("終了")
        
        

    def timejudge(self,start_time):

            end_time = time.perf_counter()
            
            # 経過時間を出力(秒)
            end_time = end_time - start_time
            #print("経過時間",end_time)
            return end_time


        

def main():
        
    mgmt=Mgmt()
    #mgmt.set_param()
    mgmt.preparation()
    mgmt.start()
        
        
if __name__ == '__main__':
    main()

