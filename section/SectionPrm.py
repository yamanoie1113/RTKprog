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
    
    def test(self):
        
        self.position.PosMgmt_init()
    

    def pointer_param(self,number):
        
        self.position.PosMgmt_init()
        print("init_OK")
        
        
        if number==1:   #Normal_Course
            
            
            param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/Normal_Pos.prm')
            
            
        elif number==2: #REIWA_Course
            
            
            param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/REIWA_Pos.prm')
            
        elif number==3:           #Circuit_Course
            
            param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/Circuit_Pos.prm')
            
        elif number==4:
            
            param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/test.prm')
            
        elif number==5:
            
            print("OK")
            
            param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/test.prm')
            
            
        #self.parameter=self.param.pointer_set_param()]
        
        param=[]
        with open(param_file, mode='r') as f:
        # parameterファイルreaderの生成
            reader = csv.reader(f)
            #reader_header=next(f)

            for prm in reader:
                param.append([elem for elem in prm])
        #print("debbb",param)
        for i in range(len(param)):
            for j in range(len(param[i])):
                
                param[i][j] = float(param[i][j])
        
        #if param[0][4]=='straight':       
        return param,self.position
        #self.pointset=self.position.PosInit()
        
        #return self.pointset,self.position
    

    def walkerset_param(self,number):
        
        #パラメータ取得
        
        if number==1:   #Normal_Course
            print("course1",number)
            param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/Normal_Course.prm')
            
            
        elif number==2: #REIWA_Course
            
            param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/REIWA_Course.prm')
            
        elif number==3:           #Circuit_Course
            
            param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/Circuit_Walk.prm')
            
            
        elif number==4:
            
            param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/Test_Straight.prm')
            
        elif number==5:
            
            param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/Test_Curve.prm')
            
        else:
            pass
        #self.parameter=self.param.pointer_set_param()
        param=[]
        with open(param_file, mode='r') as f:
            # parameterファイルreaderの生成
            reader = csv.reader(f)
            reader_header=next(f)
            # parameter readerからデータを取り出してループ
            for prm in reader:
            # strからfloatにキャストして追加
                param.append([elem for elem in prm])
                
        for i in range(len(param)):
            for j in range(len(param[i])-1):
                param[i][j] = float(param[i][j])
                
        if param[0][4]=='straight':       
            print(param[0][4])

        return param
        
    
    def walkerset_param_R(self):
        
        self.parameter=self.param.Reiwa_pointer_set_param()
        
        return self.parameter
        
    def walkerset_param_circuit(self):
        
        self.parameter=self.param.circuit_course_set_param()

        return self.parameter

def main():
    dd=SectionPrm()
    dd.pointer_param(4)
    


if __name__=="__main__":
    main()
