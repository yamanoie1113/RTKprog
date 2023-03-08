from multiprocessing import Process,Value
#from concurrent.futures import ProcessPoolExecutor
#import multiprocessing
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from yamagapractice import Test
#from section import SectionMgmt
from section import b
#from Sensors import MotorMgmt
#import Timerset
#import rpipwmtest
import time

# メインプロセスで動かす関数

class Mgmtstop:

    #signal=True
    #motormgmt=MotorMgmt.MotorMgmt()

    def __init__(self):
    
        print("プログラム開始")
        self.count = Value('i', True) #初期値１
    
    def run(self):
        print('メインプロセスStart')
        #section=SectionMgmt.SectionMgmt()

        start_time = time.perf_counter()

        #timer=1
        counter=0
        state=True #ステートの設定

        if self.count.value==False:
            print("成功1")

        else:

            #section.run()#sectionの準備
            
            while state:
                
                state2=self.timejudge1(start_time)  #時間測定

                if self.count.value==False: #プロボの電源が入ったかどうか
                    print("成功２")
                    state=False
                    break

                elif (state2>=30): #走行時間の設定 
                    state=False
                    #self.motormgmt.run(0,0)
                    break
            
                else:
                    counter+=1
                    print('tesuto')
                    #section.execRun()#section実行
                    print(counter,"回目")

        #self.GPS()

        print("終了")

        sys.exit()

    def timejudge1(self,start_time):

            end_time = time.perf_counter()

            # 経過時間を出力(秒)
            end_time = end_time - start_time
            print("経過時間",end_time)
            return end_time
        
    def end(self):
        print("all end")
        sys.exit()
        



    # 緊急停止
    def motor_stop(self):
        print('緊急停止待機状態Start')
        #statement=None
        Motor=Test.Test()
        #Motor=rpipwmtest.rpipwmtest()
        self.count.value=Motor.Re()
        #self.count.value=Motor.callb()
        print(self.count.value) #valueを使用することで変数を共有することができる

        
        '''
        for i in range(101):
            time.sleep(1)
            print(f'func_2 {i}')
        print('サブプロセス2End')
        '''

    #GPS起動
    def GPS(self):
        print("GPS_Start")
        for i in range(10):
            time.sleep(1)
            print(f'func_3 {i}')
        print('GPS_End')
        


    def main(self):
        
        p1 = Process(target=self.motor_stop)
        p2 = Process(target=self.run)
        #p3 = Process(target=self.GPS)

        
        p1.start()
        time.sleep(20)
        p2.start()
        #p3.start()


if __name__ == '__main__':
    #main()

    m=Mgmtstop()
    m.main()