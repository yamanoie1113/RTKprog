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
from section import SectionMgmt
#from section import SectionMgmt
#from Judgement import TimeJudge2

class Mgmt:
    def init(self):
    
        #self.count=0
        pass

    def run(self,section):
        
        section.__init__()
            

def main():
    mgmt=Mgmt()
    section=SectionMgmt.SectionMgmt()
    mgmt.run(section)

    

if __name__=="__main__":
    main()




    