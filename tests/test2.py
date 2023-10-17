# coding:utf-8
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
#walker_thread=None
#judge_thread=None

class test2:
    
    def run(self,pointer,po):
        #self.pointerset=pointer
        with ThreadPoolExecutor(max_workers=2) as executor:
            future = executor.submit(self.exec_run, pointer,po)
            future2= executor.submit(self.exec_judge, pointer,po)
        #walker_thread = threading.Thread(target=self.exec_run, args=(pointer,po))
        #judge_thread = threading.Thread(target=self.exec_judge, args=(pointer,po))
        #walker_thread = threading.Thread(target=self.exec_run)
        #judge_thread = threading.Thread(target=self.exec_judge)
        
        #walker_thread.start()
        #judge_thread.start()
        #walker_thread.join()
        #judge_thread.join()
        
    def exec_run(self,pointer,po):
        
        print("1",pointer,po)

    def exec_judge(self,pointer,po):
        
        print("2",pointer,po)
        
def main():
        
    mgmt=test2()
    #mgmt.timejudge1()
    mgmt.run()
    
if __name__ == '__main__':
    main()
