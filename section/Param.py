

class Param:
    def init(self):

        pass



    def Pointtest(self):

        self.pointtest([1],[2],[3],[4],[5],[6])#A,B,C,D,E,F
        


    def Straight_set_param(self,counter):

        self.prm1=([5,0,0,0],   #速度、P,I,D　
        [5,1,1,1],
        [5,1,1,1],
        [5,1,1,1],
        [None])
        #[前進量、旋回量、P,I,D]
        self.deb=self.prm1[counter]
        print("Straight",self.deb)
        #self.number+=1
        return self.deb
    
    def Curve_set_param(self,counter):
        #self.number1=0
        self.prm2=([5,6,0,0,0],
        [5,6,1,1,1],
        [None])#(前進量,旋回量,P,I,D)
        self.deb=self.prm2[counter]
        print("Curve",self.deb)
        #self.number1+=1
        return self.deb

#_______________________________________________

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

        self.pointer=([0,0], #A
        [1,0],               #B
        [2,0],               #C
        [3,0],               #D
        [4,0],               #E
        [2,0])               #C

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

    def Straight_set_param2(self):

        #速度、P,I,D　
        self.prm1=([10,0,0,0],  #A
        [10,1,1,1],             #B
        [10,2,1,1],             #C
        [10,3,1,1])             #D

        self.deb=self.prm1
        print("Straight",self.deb)
        #self.number+=1
        return self.deb

    def Curve_set_param2(self):
        #self.number1=0
        self.prm2=([5,0,0,0],
        [5,1,1,1])     #速度,P,I,D
        self.deb=self.prm2
        print("Curve",self.deb)
        #self.number1+=1
        return self.deb

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
