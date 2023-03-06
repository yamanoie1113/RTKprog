# coding:utf-8
from multiprocessing import Process, Value,Manager
#from concurrent.futures import ProcessPoolExecutor
#import multiprocessing
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from yamagapractice import Test
from section import b
#import Timerset
import time

# メインプロセスで動かす関数

class MTest:

    #signal=True

    def __init__(self):
        self.signal=Value('i', None)
        print("プログラム開始")
        pass
    
    def run(self):
        print('メインプロセスStart')
        print("GPS_Start")
        for i in range(5):
            time.sleep(1)
            print(f'run {i}')
        print(self.signal.value)
        print("終了")

    def timejudge1(self,start_time):

            end_time = time.perf_counter()

            # 経過時間を出力(秒)
            end_time = end_time - start_time
            print("経過時間",end_time)
            return end_time
        



    # 緊急停止
    def motor_stop(self):
        print('サブプロセス2Start')
        self.signal=None
        #statement=None
        Ret=Test.Test()
        self.signal.value=False
        
        #return Ret

        
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
        


    def main(self):
        
        p1 = Process(target=self.motor_stop)
        p2 = Process(target=self.run)
        #p3 = Process(target=self.GPS)

        p1.start()
        p2.start()
        #p3.start()


if __name__ == '__main__':
    #main()

    m=MTest()
    m.main()