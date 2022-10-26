import time
class d:

    curve=0
    straight=1

    def __init__(self):
        self.param=[0,1]
        self.param[0]=self.curve
        self.param[1]=self.straight
        self.p=None
        print(self.param[0])
        print(self.param[1])
        


    def set_param(self):
        self.a=4
        if self.a==0:
            self.p=self.param[0]
            print(self.p)
        else:
            self.p=self.param[1]
            print(self.p)
        
        
        


def main():

    dd=d()
    dd.set_param()

    


if __name__=="__main__":
    main()