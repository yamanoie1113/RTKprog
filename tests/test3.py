# coding:utf-8
import sys
import test2


class test3:
    
    test2ob=test2.test2()
    pointer=100
    po=10
    i=0
    
    def run(self):
        
        if self.i == 0 :
            print("start")
            self.test2ob.run(self.pointer,self.po)
            self.i=1
            self.po=1
        else:
            print("start2")
            self.i=0
            
            self.test2ob.run(self.pointer+1,self.po)
            self.po=0
        
        

def main():
        
    mgmt=test3()
    #mgmt.timejudge1()
    mgmt.run()
    
if __name__ == '__main__':
    main()
