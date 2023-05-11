# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import Param
from Sensors import PositionInitialize
#from yamagapractice import Test
class SectionPrm:
    #クラス変数
    curve=0
    straight=1
    param=Param.Param()
    position=PositionInitialize.PositionInitialize()
    #testing=Test.Test()

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

        self.pointset=self.position.update()

        print("座標です",self.pointset,"test",self.pointset[5])

        return self.pointset
    
    def pointer_paramtest(self):
        
        self.pointset=self.testing.update()
        print("座標です２",self.pointset[0])
        
        return self.pointset
        
        



    def Walkerset_param2(self,pointset):#msectionIdxは区間管理のget_paramから

        
        if pointset==0:
            self.parameter1=self.param.Straight_set_param2()
            print("walkerset1")
            return self.parameter1
            
            
        elif pointset==1:
            self.parameter2=self.param.Curve_set_param2()

            print("param",self.parameter2)

            return self.parameter2
    
    def test(self,pointset,pointset1,pointset2) :
        pass

def main():
    dd=SectionPrm()
    pointset=0
    #dd.Walkerset_param2(msectionIdx)
    dd.pointer_param()
    #dd.pointer_paramtest()
    dd.Walkerset_param2(pointset)
    pointset=1
    dd.Walkerset_param2(pointset)
    


if __name__=="__main__":
    main()
