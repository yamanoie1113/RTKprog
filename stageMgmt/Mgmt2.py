#from multiprocessing import Process
#from concurrent.futures import ProcessPoolExecutor
#import multiprocessing
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#from yamagapractice import Test
from section import SectionMgmt
from section import b
#import Timerset
#import rpipwmtest
import time

# メインプロセスで動かす関数

class Mgmt2:

    #signal=True

    def __init__(self):
    
        print("プログラム開始")
    
    def run(self):
        print('メインプロセスStart')
        section=SectionMgmt.SectionMgmt()

        start_time = time.perf_counter()

        #timer=1
        counter=0
        state=True #ステートの設定

        section.run()

        while state:
                
            state2=self.timejudge1(start_time)

            if (state2>=100): #走行時間の設定
                state=False
                break
                
            counter+=1
            print('tesuto')
            section.execRun()
            print(counter,"回目")

        print("終了")

    def timejudge1(self,start_time):

            end_time = time.perf_counter()

            # 経過時間を出力(秒)
            end_time = end_time - start_time
            print("経過時間",end_time)
            return end_time
        

    def test(self):
        section=SectionMgmt.SectionMgmt()
        section.run()
        section.test()

    # 緊急停止
    def motor_stop(self):
        print('サブプロセス2Start')
        #statement=None
        #Motor=Test.Test()
        #self.count.value=Motor.Re()
        print(self.count.value)


        
        '''
        for i in range(101):
            time.sleep(1)
            print(f'func_2 {i}')
        print('サブプロセス2End')
        '''

    #GPS起動
    def GPS(self):
        print("GPS_Start")
        for i in range(102):
            time.sleep(1)
            print(f'func_3 {i}')
        print('GPS_End')
        


def main():
        
    mgmt=Mgmt2()
    mgmt.test()
    #mgmt.run()

        #p2 = Process(target=self.motor_stop)
        #p3 = Process(target=self.GPS)

        #p1.start()
        #p2.start()
        #p3.start()

if __name__ == '__main__':
    main()

