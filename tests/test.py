# coding:utf-8
import sys
import time
import test3

class test:
    
    test3ob=test3.test3()
    
    def run(self):
        #print('メインプロセスStart')
        start_time = time.perf_counter()

        #timer=1
        counter=0
        state=True #ステートの設定

        while state:
                
            state2=self.timejudge1(start_time)
            
            self.test3ob.run()

            if (state2>=20): #走行時間の設定
                
                state=False
                break
            
            counter+=1
            #print(counter,"回目")
            
        #section.end_REIWA()

        print("終了")
    
    def timejudge1(self,start_time):

            end_time = time.perf_counter()

            # 経過時間を出力(秒)
            end_time = end_time - start_time
            #print("経過時間",end_time)
            return end_time
        
def main():
        
    mgmt=test()
    #mgmt.timejudge1()
    mgmt.run()
    
if __name__ == '__main__':
    main()
