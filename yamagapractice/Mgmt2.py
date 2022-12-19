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
from yamagapractice import SectionMgmt2
#from section import SectionMgmt
#from Judgement import TimeJudge2

class Mgmt2:
    def init(self):
    
        #self.count=0
        pass

    def run(self,section):
        
        section.__init__()
            

def main():
    mgmt=Mgmt2()
    section=SectionMgmt2.SectionMgmt2()
    mgmt.run(section)

    

if __name__=="__main__":
    main()




    