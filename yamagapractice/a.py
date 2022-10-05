from abc import ABCMeta,abstractmethod

#from Walker.Run import main
#import b


class a(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,atai1,atai2):

        self.Fpwm=atai1
        self.Tpwm=atai2
        print(self.Fpwm,self.Tpwm)

    @abstractmethod
    def set_Param(self,atai1,atai2):

        self.Fpwm=atai1
        self.Tpwm=atai2

        print(self.Fpwm,self.Tpwm)

        
        

    @abstractmethod
    def run(self,mb):
        

        print(self.Fpwm,self.Tpwm)

        mb.set_param(self.Fpwm,self.Tpwm)

    @abstractmethod
    def reset_param(self):
        self.mForward=0
        self.mTurn=0



    def main():
        print("a")
        ma=a(0,0)
        #mb=b()
        ma.set_Param(50,70)
        ma.run()
        #ma.run(mb)
        ma.reset_param()


if __name__ =="__main__":
    main()
