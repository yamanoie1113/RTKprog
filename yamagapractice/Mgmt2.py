# coding:utf-8
#from ast import Delete
#from tkinter import END
#from tracemalloc import start
#import time
#import threading
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from yamagapractice import SectionMgmt2
#from section import SectionMgmt
import Timerset
import time

class Mgmt2:
    def __init__(self):
    
        print("プログラム開始")
        pass

    def timejudge(selfe,start_time):

        end_time = time.perf_counter()

        # 経過時間を出力(秒)
        end_time = end_time - start_time
        print("経過時間",end_time)
        return end_time

    def run(self,section,timerset):
        
        start_time = time.perf_counter()

        self.timer=1
        self.counter=0
        self.state=True #ステートの設定

        while self.state:
            #elf.state2=timerset.getvalue(self.timer)
            self.state2=self.timejudge(start_time)
            #print("state2",self.state2)
            if self.state2>=180:
                self.state=False
                break
            
            self.counter+=1
            print('tesuto')
            section.run()
            print(self.counter,"回目")

        print("終了")

def main():
    mgmt=Mgmt2()
    section=SectionMgmt2.SectionMgmt2()
    timerset=Timerset.Timerset()
    mgmt.run(section,timerset)

    

if __name__=="__main__":
    main()




    