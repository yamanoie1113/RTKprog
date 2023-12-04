# coding:utf-8
import csv
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
    parameter=None
    param=Param.Param()
    position=PMgmt.PositionMgmt()
    

    def __init__(self):
        
        #test
        

        pass
    

    def pointer_param(self,number):
        
        self.position.PosMgmt_init()
        
        if number==1:   #Normal_Course
            
            pass
            #param_file=('C:\\Users\\nkhsh\\Documents\\GitHub\\RTKprog\\parameter\\Normal_Course.prm')
            
            
        elif number==2: #REIWA_Course
            
            pass
            #param_file=('C:\\Users\\nkhsh\\Documents\\GitHub\\RTKprog\\parameter\\REIWA_Course.prm')
            
        else:           #Circuit_Course
            pass
            #param_file=('C:\\Users\\nkhsh\\Documents\\GitHub\\RTKprog\\parameter\\Circuit_Course.prm')
            
        #self.parameter=self.param.pointer_set_param()]
        '''
        param=[]
        with open(param_file, mode='r') as f:
            # parameterファイルreaderの生成
                reader = csv.reader(f)
                reader_header=next(f)
            # parameter readerからデータを取り出してループ
        for prm in reader:
            param.append([elem for elem in prm])
        
        for i in range(len(param)):
            for j in range(len(param[i])-1):
                param[i][j] = float(param[i][j])
                print(param)
        
        return self.param
        self.pointset=self.position.PosInit()
        
        return self.pointset,self.position
    '''

    def walkerset_param(self,number):
        
        if number==1:   #Normal_Course
            param_file=('C:\\Users\\nkhsh\\Documents\\GitHub\\RTKprog\\parameter\\Normal_Course.prm')
            
            
        elif number==2: #REIWA_Course
            
            param_file=('C:\\Users\\nkhsh\\Documents\\GitHub\\RTKprog\\parameter\\REIWA_Course.prm')
            
        else:           #Circuit_Course
            
            param_file=('C:\\Users\\nkhsh\\Documents\\GitHub\\RTKprog\\parameter\\Circuit_Course.prm')
            
        #self.parameter=self.param.pointer_set_param()]
        
        param=[]
        with open(param_file, mode='r') as f:
            # parameterファイルreaderの生成
                reader = csv.reader(f)
                reader_header=next(f)
            # parameter readerからデータを取り出してループ
        for prm in reader:
            param.append([elem for elem in prm])
        
        for i in range(len(param)):
            for j in range(len(param[i])-1):
                param[i][j] = float(param[i][j])
                print(param)
        
        return self.param
        
    
    def walkerset_param_R(self):
        
        self.parameter=self.param.Reiwa_pointer_set_param()
        
        return self.parameter
        
    def walkerset_param_circuit(self):
        
        self.parameter=self.param.circuit_course_set_param()

        return self.parameter

def main():
    dd=SectionPrm()
    dd.pointer_param()
    dd.Walkerset_param(0)
    dd.Walkerset_param(1)
    


if __name__=="__main__":
    main()
