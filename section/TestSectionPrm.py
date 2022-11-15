# coding:utf-8
import time
import os
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
import SectionRun
from Sensors import MotorMgmt
class TestSectionPrm:
    #クラス変数
    curve=0
    straight=1

    def __init__(self):
        self.param=[0,1]
        self.param[0]=self.curve#曲線
        self.param[1]=self.straight#直線
        self.p=[0,1]#区間管理に渡す用のパラメータ
        print(self.param[0])
        print(self.param[1])
        print("section2からsectionprmのinitを呼び出した")

    def set_param(self,msectionIdx):#msectionIdxは区間管理のget_paramから
        run=SectionRun()
        

        if msectionIdx==0:
            self.p[0]=self.param[0]#曲線0
            print("set_paramです")
            
            #print("prm",self.p[0])
            run.request_Walker(self.p[0])
            
        elif msectionIdx==1:
            self.p[1]=self.param[1]#直線1
            print("prm2")
            run.request_Walker(self.p[1])
        return self.p#パラメータを返す



def main():
    dd=TestSectionPrm()
    msectionIdx=0
    dd.set_param(msectionIdx)

    


if __name__=="__main__":
    main()

    #def set_Swalker():

        

        #pass


    #def set_Cwalker():


        #pass



    
        