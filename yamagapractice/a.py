from abc import ABCMeta,abstractmethod
from yamagapractice.b import b


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
    def run(self,Fpwm,Tpwm):
        
        self.mb.set_param(Fpwm,Tpwm)

        print(Fpwm,Tpwm)


    @abstractmethod
    def reset_param(self):
        self.mForward=0
        self.mTurn=0



    def main(self):
    #self.mPID=PID(
        ma=a(0,0)
        self.mb=b()
        ma.set_Param(50,70)
        ma.run(self.Fpwm,self.Tpwm)
        ma.reset_param()
