
# coding:utf-8
#from curses.ascii import NUL
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from yamagapractice import SectionRun2
from yamagapractice import SectionPrm2
#from yamagapractice import SectionRun2

#from Walker import Run
class SectionMgmt2:
    mState=1
    UNDEFINED=1
    INIT=2
    RUN=3
    END=4
    WalkeParam=[0,0]
    Walkerinstance=[None,None]
    Judgeinstance=[None,None]
    Pointer=[None]
    
    sectionprm=SectionPrm2.SectionPrm2()
    sectionrun=SectionRun2.SectionRun2()
    STRAIGHT = 0
    CURVE = 1           #0は直線、1は曲線
    counter=0
    test0=None
    
    

    def __init__(self):

        self.Pointer=self.sectionprm.pointer_param()
        print("座標",self.Pointer)
        self.section_pointer=0
        print("initです")

    def run(self):
        
        if self.mState == self.UNDEFINED:
            print(self.mState)
            self.execUndefined()
        else:
            pass

        if self.mState == self.INIT:
            
            self.init()

        else:
            pass
        
        if self.mState == self.RUN:
            self.execRun()
        
        else:
            pass

        if self.mState==self.END:
            self.end()
            
        else:
            pass


    def execUndefined(self):

        if self.WalkeParam[0]!=[None]:

            self.mState=self.INIT

        else: 
            
            self.mState=self.END
            print("Noneでした")

    def init(self):
        
        self.flag=True
        
        self.addSection()

        print("パラム",self.WalkeParam[0])

        print("init")
        
        self.mState=self.RUN
        

    def execRun(self):
        if self.WalkeParam[0]!=[None]:
            print("Walkerのオブジェクト",self.Walkerinstance)
            print("Judgeのオブジェクト",self.Judgeinstance)
            print("Walkerのパラメータ",self.WalkeParam)
            print("座標",self.Pointer)
            self.sectionrun.run(self.Walkerinstance,self.Judgeinstance,self.WalkeParam)
            print("おわり")
            self.mState=self.END
            
        else:
                
            self.MAXpointer=self.counter
            self.mState=self.END


    def end(self):
        print(self.WalkeParam)
        print("配列確認",self.test0)
        print("カウンター=",self.counter)
        print("END")


    def addSection(self):

        self.get_Param()
        self.setWalker()
        self.setJudge()
        

    def setWalker(self):
        
        self.Walkerinstance[self.STRAIGHT]=self.sectionrun.request_Walker(self.STRAIGHT)

        self.Walkerinstance[self.CURVE]=self.sectionrun.request_Walker(self.CURVE)
        

        print("Walkerinstanceです",self.Walkerinstance)
        print("WalkerParamです",self.WalkeParam)


    def setJudge(self):
        
        self.Judgeinstance[self.STRAIGHT]=self.sectionrun.request_judge(self.STRAIGHT)
        
        self.Judgeinstance[self.CURVE]=self.sectionrun.request_judge(self.CURVE)

        print("Judgeinstanceです",self.Judgeinstance)
        


    def get_Param(self):
        
        #self.test0=None

        self.WalkeParam[self.STRAIGHT]=self.sectionprm.Walkerset_param(self.STRAIGHT,self.counter)

        self.WalkeParam[self.CURVE]=self.sectionprm.Walkerset_param(self.CURVE,self.counter)

        #デバッグ
        if self.counter==5:
            self.test0=self.WalkeParam[self.CURVE]
            

        self.counter+=1

        print(self.test0)
        print("カウンター=",self.counter)





def main():
    sectionMgmt=SectionMgmt2()
    #pointing=2
    sectionMgmt.run()
    
    

if __name__=="__main__":
    main()



