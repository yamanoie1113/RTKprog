#from multiprocessing import Process
#from concurrent.futures import ProcessPoolExecutor
#import multiprocessing
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#from yamagapractice import Test
from section import SectionMgmt

#import Timerset
#import rpipwmtest
import time

# メインプロセスで動かす関数

class Mgmt:

    #signal=True

    def __init__(self):
    
        print("プログラム開始")
    
    def run(self):
        #print('メインプロセスStart')
        section=SectionMgmt.SectionMgmt()

        

        #timer=1
        #counter=0
        state=True #ステートの設定

        section.run()

        while state:
            
            start_time = time.perf_counter()
            
            state2=self.timejudge1(start_time)
            
            if (state2>=50): #走行時間の設定
                state=False
                break
                
            section.execRun()

            #周期の秒数
            print("秒数",time.perf_counter()-start_time)
            
            #秒数の計算
            if (time.perf_counter()-start_time)>= 0.5:
                
                time.sleep((time.perf_counter()-start_time)-0.5)
            
            else:
                
                pass
            
                

        print("終了")
        
        

    def timejudge1(self,start_time):

            end_time = time.perf_counter()
            #
            # 経過時間を出力(秒)
            end_time = end_time - start_time
            #print("経過時間",end_time)
            return end_time
        
    def timejudge2(self,start_set_time):
        
        pass
        

    def test(self):
        section=SectionMgmt.SectionMgmt()
        section.run()
        section.test()


        


def main():
        
    mgmt=Mgmt()
    #mgmt.test()
    mgmt.run()
        #p1 = threading(target=self.run)
        #p2 = threading(target=self.motor_stop)
        #p3 = Process(target=self.GPS)

        #p1.start()
        #p2.start()
        #p3.start()

if __name__ == '__main__':
    main()

