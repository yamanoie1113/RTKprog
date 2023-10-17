# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import Param
from Sensors import PositionMgmt as PMgmt

class SectionPrm:
    #クラス変数
    curve=0
    straight=1
    param=Param.Param()
    position=PMgmt.PositionMgmt()

    def __init__(self):
        
        #test
        

        pass
    

    def pointer_param(self):
        #print("param")
        self.pointset=self.position.PosInit()
        #print(self.pointset)
        #print("print_OK")
        #print(self.pointset[0])

        return self.pointset
    
    def pointer_param_R(self):

        
        self.pointset=self.position.REIWA()

        #print(self.pointset[0])

        return self.pointset
    
    


    def Walkerset_param(self,pointset):#msectionIdxは区間管理のget_paramから

        
        if pointset==0:
            self.parameter1=self.param.Straight_set_param()
            
            return self.parameter1
        
        
        
            
            
        else:
            self.parameter2=self.param.Curve_set_param()
        
            return self.parameter2
        
    
    def walkerset_param_R(self,pointset):
        
        if pointset==0:
            self.parameter1=self.param.Reiwa_Straight()
            
            return self.parameter1
        
            
            
        else:
            self.parameter2=self.param.Reiwa_Curve()
        
            return self.parameter2
        
        
    

def main():
    dd=SectionPrm()
    dd.pointer_param()
    dd.Walkerset_param(0)
    dd.Walkerset_param(1)
    


if __name__=="__main__":
    main()
