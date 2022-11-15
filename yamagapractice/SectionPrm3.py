# coding:utf-8
import time
import os
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#from Sensors import MotorMgmt
class SectionPrm3:
    #クラス変数
    curve=0
    straight=1

    def __init__(self):
                                #前進量、旋回量、P,I,D           前進量、P,I,D
        self.list_section = [self.curve,[0,0,0,0,0],self.straight,[0,0,0,0]]#list_section[0]が曲線
        self.pr=[None]              #↑ごめん多分これ２５６こくらい要素作って値設定していくのかもしれん。わからん


        pass

    def set_param(self,msectionIdx):#msectionIdxは区間管理のget_paramから
        if msectionIdx==0:
            self.number=1 #ごめんこれはinitでめんどくさいことしちゃったから
            self.pr=self.list_section[self.number]#self.prに[0,0,0,0,0]を入れる
            print("set_param値",self.pr)
            
        elif msectionIdx==1:
            self.number=3
            self.pr=self.list_section[self.number]
            print("set_param値",self.pr)
            
        return self.pr
            
        

    


def main():
    msectionIdx=0
    dd=SectionPrm3()
    dd.set_param(msectionIdx)
    pass
    


if __name__=="__main__":
    main()

    #def set_Swalker():

        

        #pass


    #def set_Cwalker():


        #pass



    
        