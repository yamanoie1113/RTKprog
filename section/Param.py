

class Param:
    def init(self):

        pass

#_______________REIWA_______________________________

    def Reiwa_Straight(self):

        self.Rprm_straight=([5,0,0,0],
        [5,0,0,0],
        [5,0,0,0],
        [5,0,0,0],
        [5,0,0,0],
        [5,0,0,0],
        [5,0,0,0])

        return self.Rprm_straight


    def Reiwa_Curve(self):

        self.Rprm_curve=([5,0,0,0],
        [5,0,0,0])

        return self.Rprm_curve



    def pointer_set_param(self):

        self.pointer=([17,8], #A
        [1,0],               #B
        [2,0],               #C chusin
        [3,0],               #D
        [4,0],               #E
        [2,0])               #C chusin

        return  self.pointer

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
        

#_________________NEW______________________________

    def Straight_set_param2(self):

        #速度、P,I,D　
        self.prm1=([30,0,0,0],  #A
        [0,1,1,1],              #B
        [10,2,1,1],             #C
        [10,3,1,1])             #D
        
        return self.prm1

    def Curve_set_param2(self):
        
        self.prm2=([5,0,0,0],[5,1,1,1])   #速度,P,I,D
        

        return self.prm2

    def Reiwa_straight_set_param(self):
        
        self.Rstraightprm=([])
        
        pass

    def Reiwa_curve_set_param(self):

        self.Lstraightparam=([])

        pass

def main():
    #param=Param2.Param2
    param=Param()
    counter=0
    param.Curve_set_param(counter)
    


if __name__=="__main__":
    main()
