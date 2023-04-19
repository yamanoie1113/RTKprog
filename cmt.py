# coding:utf-8
from multiprocessing import Process
import os
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
import rpipwmtest
#import pigpio



def main():
    print("b")
    rpip = rpipwmtest.rpipwmtest()
    rpip.callb()
    print("v")
    
def ant():
    print("d")
    return False
        
if __name__ == '__main__':
    main()
