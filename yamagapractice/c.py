import time
class C:

    curve=0
    straight=1
    def init(self):
        
        self.param[0,1]
        self.p=None
        


    def set_param(self):
        self.t=time.time
        #time(10)
        a=0
        if a==self.curve:#curve=0
            self.p[0]=self.param[self.curve]#p[0]←0
            if self.t==10:#time
                self.p=self.param[self.straight]#straight=1
                print(self.p)
                self.t=0#ゼロに戻したい
                print(self.t)
        elif a==self.straight:#staraight=1
            self.p=self.param[self.straight]#Param←1
            print(self.p)
            if self.t==10:#time
                self.p=self.param[self.curve]
                self.t=0#ゼロに戻したい
                print(self.t)
        


def main():

    cc=C()
    cc.set_param()

    pass


if __name__=="__main__":
    main()




    curve=0
    straight=1
    def init(self):

        self.param=[0,1]
        self.param[0]=[self.curve]
        self.param[1]=[self.straight]
        self.Pa=None
        #0がカーブ
        #1が直進

    def set_param(self):
        #mMotorMgmt=MotorMgmt()
        self.t=time.time
        a=0
        #time(10)
        if a==self.param[0]:#curve=0
            self.Pa=self.param[0]#Param←0
            if self.t==10:#time
                self.Pa=self.param[1]#straight=1
                self.t=0#ゼロに戻したい
        elif a==self.param[1]:#staraight=1
            self.Pa=self.param[1]#Param←1
            if self.t==10:#time
                self.Pa=self.param[0]
                self.t=0#ゼロに戻したい
        
        
        return self.Pa

def main():

    dd=SectionPrm()
    dd.set_param()

    


if __name__=="__main__":
    main()