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
from yamagapractice import SectionMgmt3
#from section import SectionMgmt
#import Timerset
import time

class Mgmt3:

    def __init__(self):
    
        print("プログラム開始")
        pass

    def timejudge1(self,start_time):

        end_time = time.perf_counter()

        # 経過時間を出力(秒)
        end_time = end_time - start_time
        print("経過時間",end_time)
        return end_time

    def run(self):
        print('メインプロセスStart')
        section=SectionMgmt3.SectionMgmt3()

        start_time = time.perf_counter()

        #timer=1
        counter=0
        state=True #ステートの設定

        section.run()

        while state:
            
            state2=self.timejudge1(start_time)

            if state2>=2: #走行時間の設定
                state=False
                break
            
            counter+=1
            print('tesuto')
            section.execRun()
            print(counter,"回目")

        print("終了")

    def timejudge1(start_time):

        end_time = time.perf_counter()

        # 経過時間を出力(秒)
        end_time = end_time - start_time
        print("経過時間",end_time)
        return end_time
        


def main():
    mgmt=Mgmt3()
    

    mgmt.run()

    

if __name__=="__main__":
    main()




    