

class Param:
    
    def init(self):

        pass



#_________________PARAMETER______________________________

#直進 （速度、P,I,D）


    def pointer_set_param(self):

        self.pointer=([25,1,0.4,1], #A
        [20,1,0.4,1],               #B
        [25,1,0.4,1],               #C 中心
        [25,1,0.4,1],               #D
        [20,1,0.4,1],               #E
        [25,1,0.4,1])               #C 中心

        return  self.pointer


#_______________REIWA_pointer_______________________________


    def Reiwa_pointer_set_param(self):
        self.Reiwa_pointetr=([25,1,0.4,1], #A
        [20,1,0.4,1],                      #B
        [25,1,0.4,1],                      #C サブパイロン通過
        [25,1,0.4,1],                      #D
        [20,1,0.4,1],                      #E
        [25,1,0.4,1],)                     #F　サブパイロン通過
        
        return self.Reiwa_pointetr
    
    
#______________サーキットコース_______________________________


    def circuit_course_set_param(self):
        
        self.circuit_pointer=([25,1,0.4,1], #A
        [25,1,0.4,1],                       #B
        [25,1,0.4,1])                       #C
        
        return self.circuit_pointer


'''

    def Straight_set_param(self):

        #速度、P,I,D
        self.prm1=([25,1,0.4,1],  #C-A 1
        [25,1,0.4,1],             #B-C 3
        [25,1,0.4,1],             #C-D 4
        [25,1,0.4,1])             #E-C 6
        
        return self.prm1

#曲線（速度、P,I,D）

    def Curve_set_param(self):
        
        self.prm2=([20,1,0.4,1], #A-B 2
                [20,1,0.4,1])    #D-E 5

        return self.prm2

'''

def main():
    #param=Param2.Param2
    param=Param()
    counter=0
    param.Curve_set_param(counter)
    


if __name__=="__main__":
    main()

