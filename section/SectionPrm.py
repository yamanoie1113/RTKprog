# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import Param
from Sensors import PosInit

class SectionPrm:
    #クラス変数
    curve=0
    straight=1
    param=Param.Param()
    position=PosInit.PositionInitialize()

    def __init__(self):

        pass
    

    def pointer_param(self):

        self.pointset=self.position.update()

        print("座標です",self.pointset,"\n""test",self.pointset[5])

        return self.pointset


    def Walkerset_param2(self,pointset):#msectionIdxは区間管理のget_paramから

        
        if pointset==0:
            self.parameter1=self.param.Straight_set_param2()
            print("walkerset1",self.parameter1)
            return self.parameter1
            
            
        elif pointset==1:
            self.parameter2=self.param.Curve_set_param2()

            print("param",self.parameter2)

            return self.parameter2

def main():
    dd=SectionPrm()
    dd.pointer_param()
    dd.Walkerset_param2(0)
    dd.Walkerset_param2(1)
    


if __name__=="__main__":
    main()
