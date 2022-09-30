from yamagapractice.a import a


class b(a):
    def __init__(self):
        self.atai1=4
        self.atai2=0
        print(self.atai1,self.atai2)

    def set_param(self,atai6,atai7):
        print(self.atai1,self.atai2)
        self.atai1=self.atai1 + atai6
        self.atai2=5+atai7
        print(self.atai1,self.atai2)

mb=b()
mb.set_param()

    

