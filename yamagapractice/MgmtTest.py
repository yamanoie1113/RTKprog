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
from yamagapractice import SMgmt
#from yamagapractice import SectionMgmt3
#from section import SectionMgmt
#import Timerset
import time

class MgmtTest:

    def __init__(self):
    
        print("プログラム開始")
        pass

    def timejudge(selfe,start_time):

        end_time = time.perf_counter()

        # 経過時間を出力(秒)
        end_time = end_time - start_time
        print("経過時間",end_time)
        return end_time

    def run(self):
        
        section=SMgmt.SMgmt()
        start_time = time.perf_counter()

        self.timer=1
        self.counter=0
        self.state=True #ステートの設定

        section.run()

        while self.state:
            
            self.state2=self.timejudge(start_time)

            if self.state2>=60: #走行時間の設定
                self.state=False
                #sys.exit('end')
                break
            
            self.counter+=1
            print('tesuto')
            section.execRun()
            print(self.counter,"回目")

        print("終了")

def main():
    mgmt=MgmtTest()
    

    mgmt.run()

    

if __name__=="__main__":
    main()




    