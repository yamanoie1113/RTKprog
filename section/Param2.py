

class Param2:
    def init(self):
        
        print("init通りました")

    def Curve_set_param(self,count):

        self.prm=([5,6,0,0,0],
        [5,6,1,1,1],
        [5,2,1,1,1],
        [5,1,1,1,1],
        [None])
        #[前進量、旋回量、P,I,D]
        self.deb=self.prm[count]
        print("Curve",self.deb)
        #self.number+=1
        return self.deb
    
    def Straight_set_param(self,count):
        #self.number1=0
        self.prm=([5,0,0,0,0],
        [5,0,1,1,1],
        [5,0,1,1,1],
        [5,0,1,1,1],
        [None])#(前進量,旋回量,P,I,D)
        self.deb=self.prm[count]
        #self.number1+=1
        print("straight",self.deb)

        return self.deb

    def count_set_param1(self,counting):
        #self.number2=0
        print("xxxxxxxxxxx",counting)
        self.cnt=(1,4,4,4,4,5,4,6,3,7,3,8,3,9,3,10,None)
        self.count=self.cnt[counting] 
        print("カウントの秒数",self.cnt[counting])
        #self.number2+=1
        return  self.count

    def count_set_param2(self,counting):
        #self.number2=0
        print("xxxxxxxxxxx",counting)
        self.cnt=(2,5,2,3,2,2,2,5,7,4,5,7,2,6,3,11,None)
        self.count=self.cnt[counting] 
        print("カウントの秒数",self.cnt[counting])
        #self.number2+=1
        return  self.count