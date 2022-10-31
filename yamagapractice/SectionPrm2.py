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
        self.p=[0]#区間管理に渡す用のパラメータ
        #msectionIdx=0
        print(self.p)
        

    def set_param(self,msectionIdx):#msectionIdxは区間管理のget_paramから
    

        if msectionIdx==0:
            self.p[0]=self.param[0]#曲線0
            print(self.p)
            
            
        elif msectionIdx==1:
            self.p[1]=self.param[1]#直線1
            print(self.p)
        
        return self.p#パラメータを返す
        

        
        #if msectionIdx==0:
        #オブジェクト生成()
            #rtrace=VirtualLineTrace()
            #ctrace=curvelineTrace()
            #rtrace.run()
            
            #crtrace.run()
            
            
        #時間設定して実行するのは区間パラメータでははないのかも



def main():
    msectionIdx=0
    dd=SectionPrm2()
    dd.set_param(msectionIdx)

    


if __name__=="__main__":
    main()

    #def set_Swalker():

        

        #pass


    #def set_Cwalker():


        #pass



    
        