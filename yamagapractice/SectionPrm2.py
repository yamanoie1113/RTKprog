# coding:utf-8
import time
import os
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
import Param2
#from Sensors import MotorMgmt
class SectionPrm2:
    #クラス変数
    curve=0
    straight=1
    param=Param2.Param2()


    def __init__(self):



        pass

    def Walkerset_param(self,pointset,msectionIdx):#msectionIdxは区間管理のget_paramから

        
        if pointset==0:
            self.parameter=self.param.Straight_set_param(msectionIdx)
        elif pointset==1:
            self.parameter=self.param.Curve_set_param(msectionIdx)

        print("param",self.parameter)

        return self.parameter


    def pointer_param(self):

        self.pointset=self.param.pointer_set_param()

        print("座標です",self.pointset)

        return self.pointset



    def Walkerset_param2(self,pointset):#msectionIdxは区間管理のget_paramから

        
        if pointset==0:
            self.parameter=self.param.Straight_set_param2()
        elif pointset==1:
            self.parameter=self.param.Curve_set_param2()

        print("param",self.parameter)

        return self.parameter

def main():
    #param=Param2.Param2
    dd=SectionPrm2()
    msectionIdx=1
    dd.Walkerset_param(msectionIdx)
    


if __name__=="__main__":
    main()

    #def set_Swalker():

        

        #pass


    #def set_Cwalker():


        #pass



    
        