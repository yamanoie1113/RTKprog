import csv

class test:


    def __init__(self):
        
        #test

        pass
    
    def pointer_param(self):
        
            
        #param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/Test_Straight_Pos.prm')
        param_file = ('/Users/student/Documents/GitHub/RTKprog/parameter/Test_Straight_Pos.prm')

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
        

        print(param)
        #if param[0][4]=='straight':       
        #self.pointset=self.position.PosInit()
        
        #return self.pointset,self.position
    

    

def main():
    dd=test()
    dd.pointer_param()
    


if __name__=="__main__":
    main()
