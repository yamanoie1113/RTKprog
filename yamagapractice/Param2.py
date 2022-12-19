

class Param2:
    def init(self):

        pass

    def Curve_set_param(self):
        
        self.prm=([5,100,0,0,0],
        [5,-100,1,1,1],
        [5,50,1,1,1],
        [5,-50,1,1,1],
        [999])
        #[前進量、旋回量、P,I,D]
        self.deb=self.prm
        print("Curve",self.deb)

        return self.deb
    
    def Straight_set_param(self):

        self.prm=([5,0,0,0,0],
        [5,0,1,1,1],
        [5,0,1,1,1],
        [5,0,1,1,1],
        [999])#(前進量,旋回量,P,I,D)
        self.deb=self.prm
        print("straight",self.deb)

        return self.deb

    def count_set_param(self):

        self.cnt=[10,5,8,9,11,16,16,20,999]

        return  self.cnt