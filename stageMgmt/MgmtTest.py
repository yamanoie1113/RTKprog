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
from section import SectionMgmtTest
#from section import SectionMgmt
from Judgement import TimeJudge

class MgmtTest:
    def init(self):
    
        #self.count=0
        pass

    def run(self,section):
        self.count=0
        self.state=True
        self.time=60
        self.timeMgmt=TimeJudge.TimeJudge()
        self.statment=self.timeMgmt.judge(self.time)
        while self.state:

            #if self.count==5:
                #self.count=0
                print("終了")
                #self.state=False
            #else:
                #self.mstate=0
                section.__init__()
                print(self.count,"回目")
                self.count+=1
                if self.statment==False:
                    self.state==False
                    break

def main():
    mgmt=MgmtTest()
    section=SectionMgmtTest.SectionMgmtTest()
    mgmt.run(section)

    

if __name__=="__main__":
    main()




    