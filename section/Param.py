# coding: utf-8 

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




#_______________REIWA_PARAMETER_______________________________

#直線

    def Reiwa_Straight(self):
        
        self.Rprm_straight=([35,1,0.4,1], #A
        [35,1,0.4,1],                     #C
        [35,1,0.4,1],                     #D                    
        [35,1,0.4,1],)                     #S
        return self.Rprm_straight

#曲線

    def Reiwa_Curve(self):

        self.Rprm_curve=([40,1,0.4,1], #B
        [40,1,0.4,1])                  #F

        return self.Rprm_curve

#_______________test_pointer_______________________________


    def pointer_set_param(self):

        self.pointer=([17,8], #A
        [1,0],               #B
        [2,0],               #C chusin
        [3,0],               #D
        [4,0],               #E
        [2,0])               #C chusin

        return  self.pointer


#_______________test_REIWA_pointer_______________________________


    def Reiwa_pointer_set_param(self):
        self.Reiwa_pointetr=([0,0], #A
        [0,0],                      #B
        [0,0],                      #C
        [0,0],                      #D
        [0,0],                      #E
        [0,0],                      #F
        [0,0],                      #G
        [0,0],                      #H
        [0,0])                      #I

        return self.Reiwa_pointetr


#__________________________________________________________

def main():
    #param=Param2.Param2
    param=Param()
    counter=0
    param.Curve_set_param(counter)
    


if __name__=="__main__":
    main()

