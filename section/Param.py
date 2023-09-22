

class Param:
    
    def init(self):

        pass


#_________________PARAMETER______________________________

#直進 （速度、P,I,D）

    def Straight_set_param(self):

        #速度、P,I,D　
        self.prm1=([20,0,0,0],  #C-A 1
        [30,1,1,1],             #B-C 3
        [30,2,1,1],             #C-D 4
        [30,3,1,1])             #E-C 6
        
        return self.prm1

#曲線　（速度、P,I,D）

    def Curve_set_param(self):
        
        self.prm2=([20,20,0,0,0], #A-B 2
                [20,20,1,1,1])    #D-E 5

        return self.prm2


#_______________REIWA_PARAMETER_______________________________

#直線

    def Reiwa_Straight(self):
        
        self.Rprm_straight=([5,0,0,0], #A
        [5,0,0,0],                     #C
        [5,0,0,0],                     #D
        [5,0,0,0],                     #E
        [5,0,0,0],                     #G
        [5,0,0,0],                     #H
        [5,0,0,0])                     #S

        return self.Rprm_straight

#曲線

    def Reiwa_Curve(self):

        self.Rprm_curve=([5,60,0,0,0], #B
        [5,50,0,0,0])                  #F

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

