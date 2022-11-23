

class Param:
    def init(self):

        pass

    def Curve_set_param(self):
        
        self.prm=([5,6,0,0,0],
        [5,6,1,1,1],
        [5,2,1,1,1],
        [5,1,1,1,1])
        #[前進量、旋回量、P,I,D]
        self.deb=self.prm
        print("Curve",self.deb)

        return self.deb
    
    def Straight_set_param(self):

        self.prm=([5,0,0,0,0],
        [5,0,1,1,1],
        [5,0,1,1,1],
        [5,0,1,1,1])#(前進量,旋回量,P,I,D)
        self.deb=self.prm
        print("straight",self.deb)

        return self.deb

    def count_set_param(self):

        self.cnt=(2,4,4,4,4,4,4,4)

        return  self.cnt