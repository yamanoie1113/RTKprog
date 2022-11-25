

class Param2:
    def init(self):
        
        print("init通りました")

    def Curve_set_param(self):
        self.number=0
        self.prm=([5,6,0,0,0],
        [5,6,1,1,1],
        [5,2,1,1,1],
        [5,1,1,1,1])
        #[前進量、旋回量、P,I,D]
        self.deb=self.prm[self.number]
        print("Curve",self.deb)
        self.number+=1
        return self.deb
    
    def Straight_set_param(self):
        self.number1=0
        self.prm=([5,0,0,0,0],
        [5,0,1,1,1],
        [5,0,1,1,1],
        [5,0,1,1,1])#(前進量,旋回量,P,I,D)
        self.deb=self.prm[self.number1]
        self.number1+=1
        print("straight",self.deb)

        return self.deb

    def count_set_param(self):
        self.number2=0
        self.cnt=(2,4,4,4,4,4,4,4)
        self.count=self.cnt[self.number2]
        self.number2+=1
        return  self.cnt