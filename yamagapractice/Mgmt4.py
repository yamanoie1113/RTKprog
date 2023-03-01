from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor
#import multiprocessing
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from yamagapractice import SectionMgmt3
#from section import SectionMgmt
#import Timerset
import time

# メインプロセスで動かす関数

class Mgmt4:

    def __init__(self):
    
        print("プログラム開始")
        pass
    
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

            if state2>=100: #走行時間の設定
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
        



    # サブプロセスで動かす関数
    def func_2(self):
        print('サブプロセス2Start')
        for i in range(101):
            time.sleep(1)
            print(f'func_2 {i}')
        print('サブプロセス2End')


    def func_3(self):
        print("サブプロセス3Start")
        for i in range(102):
            time.sleep(1)
            print(f'func_3 {i}')
        print('サブプロセス3End')
        


    def main(self):
        p1 = Process(target=self.run)
        p2 = Process(target=self.func_2)
        p3 = Process(target=self.func_3)

        p1.start()
        p2.start()
        p3.start()


if __name__ == '__main__':
    #main()

    m=Mgmt4()
    m.main()