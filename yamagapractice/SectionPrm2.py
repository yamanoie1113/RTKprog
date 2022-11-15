# coding:utf-8
import time
import os
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#from Sensors import MotorMgmt
class SectionPrm2:
    #クラス変数
    curve=0
    straight=1

    def __init__(self):
        self.param=[0,1]
        self.param[0]=self.curve#曲線
        self.param[1]=self.straight#直線
        self.p=[0,1]#区間管理に渡す用のパラメータ
        print(self.param)
        print("section2からsectionprmのinitを呼び出した")

    def set_param(self,msectionIdx):#msectionIdxは区間管理のget_paramから
    

        if msectionIdx==0:
            self.p[msectionIdx]=self.param[0]#曲線0
            print("set_paramです")
            #print("prm",self.p[0])
            
            
        elif msectionIdx==1:
            self.p[msectionIdx]=self.param[1]#直線1
            print("prm2")
        
        return self.p[msectionIdx]#パラメータを返す



#def main():
    #msectionIdx=0
    #dd=SectionPrm2()
    #dd.set_param(msectionIdx)

    


#if __name__=="__main__":
    #main()

    #def set_Swalker():

        

        #pass


    #def set_Cwalker():


        #pass



    
        