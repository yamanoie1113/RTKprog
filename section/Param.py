

class Param:
    
    def init(self):

        pass


#_________________PARAMETER______________________________

#直進 （速度、P,I,D）

    def Straight_set_param(self):

        #速度、P,I,D
        self.prm1=([35,1,0.4,1],  #C-A 1
        [35,1,0.4,1],             #B-C 3
        [35,1,0.4,1],             #C-D 4
        [35,1,0.4,1])             #E-C 6
        
        return self.prm1

#曲線　（速度、P,I,D）

    def Curve_set_param(self):
        
        self.prm2=([40,1,0.4,1], #A-B 2
                [40,1,0.4,1])    #D-E 5

        return self.prm2


#_______________REIWA_PARAMETER_______________________________

#直線

    def Reiwa_Straight(self):
        
        self.Rprm_straight=([35,1,0.4,1], #A
        [35,1,0.4,1],                     #C
        [35,1,0.4,1],                     #D                     #E                    #G
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

