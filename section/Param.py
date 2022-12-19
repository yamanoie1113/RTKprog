

class Param:
    def init(self):

        pass

    def Curve_set_param(self):
        
        self.prm=([5,100,0,0,0],
        [7,-100,1,1,1],
        [5,50,1,1,1],
        [3,-50,1,1,1],
        [999])
        #[前進量、旋回量、P,I,D]
        self.deb=self.prm
        print("Curve",self.deb)

        return self.deb
    
    def Straight_set_param(self):

        self.prm=([6,0,0,0,0],
        [5,0,1,1,1],
        [5,0,1,1,1],
        [5,0,1,1,1],
        [999])#(前進量,旋回量,P,I,D)
        self.deb=self.prm
        print("straight",self.deb)

        return self.deb

    def count_set_param(self):

        self.cnt=[10,7,8,9,5,13,7,6,999]

        return  self.cnt