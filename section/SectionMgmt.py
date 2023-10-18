
# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import SectionRun
from section import SectionPrm
#from Walker import Run

class SectionMgmt:
    mState=1
    UNDEFINED=1
    INIT=2
    RUN=3
    END=4
    WalkeParam=[0,0]
    Walkerinstance=[None,None]
    Judgeinstance=[None,None]
    Pointer=None
    
    sectionprm=SectionPrm.SectionPrm()
    sectionrun=SectionRun.SectionRun()
    STRAIGHT = 0
    CURVE = 1           #0は直線、1は曲線
    counter=0
    test0=None
    section_set=[0,1,0,0,1,0]    #0が直線　1が曲線
    section_set_Reiwa=[0,1,0,0,0,1,0,0,0]
    

    def __init__(self):

        pass

    def run(self):
        #print("runcheck")
        if self.mState == self.UNDEFINED:
            #print(self.mState)
            self.execUndefined()
        else:
            pass

        if self.mState == self.INIT:
            #print("SECTION_INIT")
            self.init()

        else:
            pass
        
        if self.mState == self.RUN:
            #print("execRuncheck")
            self.execRun()
        
        else:
            pass

        if self.mState==self.END:
            self.end()
            
        else:
            pass


    def execUndefined(self):
        #print("UNDEF")
            
        self.mState=self.INIT


    def init(self):
        
        self.flag=True
        
        self.addSection()

        self.section=0
        self.sectionpoint=0
        self.instancepoint=0
        self.Swalkerpointer=0 #6まで
        self.Cwalkerpointer=0 #2まで
        self.pointerset=0
        self.testsection=1
    
    def test1(self):#直進テスト
        
        #prin("test")
        self.sectionrun.test_straight(self.Walkerinstance[0],self.Judgeinstance[0],
                                    self.WalkeParam[0][0],self.Pointer[0]) 
        
    def test2(self):#曲線テスト
            print("Walkerinstance:",self.Walkerinstance[self.STRAIGHT])
            print("judgeinstance",self.Judgeinstance[self.STRAIGHT])
            print("WalkerParam",self.WalkeParam)
            print("座標",self.Pointer)
        #self.sectionrun.test_curve(self.Walkerinstance[1],self.Judgeinstance[1],self.WalkeParam[1][0],self.Pointer[1])
        #print("curvetest",self.WalkeParam[1][0],self.Pointer[1])
        
    def execRun(self):
        
        #パラメータの配列を最初に戻すのを繰り返す
        
        if self.section_set[self.pointerset]==0: #直線の場合
            self.section=0
            '''
            print("Walkerinstance:",self.Walkerinstance[self.STRAIGHT])
            print("judgeinstance",self.Judgeinstance[self.STRAIGHT])
            print("WalkerParam",self.WalkeParam[self.STRAIGHT][self.Swalkerpointer])
            print("座標",self.Pointer[self.pointerset])
            '''
            self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                    self.WalkeParam[self.STRAIGHT][self.Swalkerpointer],self.Pointer[self.pointerset]) 

            self.Swalkerpointer+=1
            if self.Swalkerpointer==4:
                self.Swalkerpointer=0

            self.pointerset+=1
            if self.pointerset==6:
                self.pointerset=0
                

                
        else: #曲線
            '''
            print("Walkerinstance:",self.Walkerinstance[self.CURVE])
            print("judgeinstance",self.Judgeinstance[self.CURVE])
            print("WalkerParam",self.WalkeParam[self.CURVE][self.Cwalkerpointer])
            print("座標",self.Pointer[self.pointerset])
            '''
            
            self.sectionrun.run(self.Walkerinstance[self.CURVE],self.Judgeinstance[self.CURVE],
                                    self.WalkeParam[self.CURVE][self.Cwalkerpointer],self.Pointer[self.pointerset])

            self.Cwalkerpointer+=1
            if self.Cwalkerpointer==2:
                self.Cwalkerpointer=0

            self.pointerset+=1
            if self.pointerset==6:
                self.pointerset=0

        self.mState=self.END
        
    def excecRun_R(self):
        
        if self.section_set_Reiwa[self.pointerset]==0: #直線の場合
            '''
            print("走行インスタンス",self.Walkerinstance[self.STRAIGHT])
            print("判定インスタンス",self.Judgeinstance[self.STRAIGHT])
            print("パラメータ",self.WalkeParam[self.STRAIGHT][self.Swalkerpointer])
            print("座標",self.Pointer[self.pointerset])
            '''
            stete=self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                    self.WalkeParam[self.STRAIGHT][self.Swalkerpointer],self.Pointer[self.pointerset],self.section_set_Reiwa[self.pointerset]) 
            
        
            self.Swalkerpointer+=1
            if self.Swalkerpointer==6:  
                self.Swalkerpointer=0

            self.pointerset+=1
            if self.pointerset==8:
                self.pointerset=0
                

                
        else: #曲線
            
            self.sectionrun.run(self.Walkerinstance[self.CURVE],self.Judgeinstance[self.CURVE],
                                    self.WalkeParam[self.CURVE][self.Cwalkerpointer],self.Pointer[self.pointerset],self.section_set_Reiwa[self.pointerset])

            self.Cwalkerpointer+=1
            if self.Cwalkerpointer==2:
                self.Cwalkerpointer=0

            self.pointerset+=1
            if self.pointerset==8:
                self.pointerset=0

        self.mState=self.END
        
        pass

    def end(self):
        
        self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                    self.WalkeParam[self.STRAIGHT][self.Swalkerpointer],self.Pointer[self.pointerset],self.section_set_Reiwa[self.pointerset]) 
        
        
        
        
    
    def end_REIWA(self):
        
        
        self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                    self.WalkeParam[self.STRAIGHT][self.Swalkerpointer],self.Pointer[self.pointerset],self.section_set_Reiwa[self.pointerset]) 
        
        
        
        
        


    def addSection(self):
        #print("addsection1")
        self.get_Param()#座標、パラメータ
        self.setWalker()#instaance
        #print("addsection2")
        self.setJudge()#判定
        #print("addsection3")
    
    def addSection_R(self):
        
        self.get_Param_R()#座標、パラメータ
        self.setWalker()#instance
        self.setJudge()#判定
        
        pass
        

    def setWalker(self):
        
        #print("walkeinstance")
        self.Walkerinstance[self.STRAIGHT]=self.sectionrun.request_Walker(self.STRAIGHT)

        self.Walkerinstance[self.CURVE]=self.sectionrun.request_Walker(self.CURVE)



    def setJudge(self):
        
        self.Judgeinstance[self.STRAIGHT]=self.sectionrun.request_judge(self.STRAIGHT)
        
        self.Judgeinstance[self.CURVE]=self.sectionrun.request_judge(self.CURVE)

        
        


    def get_Param(self):
        #print("get_walkeparam")
        self.WalkeParam[self.STRAIGHT]=self.sectionprm.Walkerset_param(self.STRAIGHT)

        self.WalkeParam[self.CURVE]=self.sectionprm.Walkerset_param(self.CURVE)

        self.Pointer=self.sectionprm.pointer_param()
        #print("pointer")
        
    def get_Param_R(self):
        
        self.WalkeParam[self.STRAIGHT]=self.sectionprm.walkerset_param_R(self.STRAIGHT)

        self.WalkeParam[self.CURVE]=self.sectionprm.walkerset_param_R(self.CURVE)

        self.Pointer=self.sectionprm.pointer_param_R()







def main():
    #print("teststart")
    sectionMgmt=SectionMgmt()
    sectionMgmt.run()
    #sectionMgmt.execRun()
    #sectionMgmt.test1()
    sectionMgmt.test2()
    

if __name__=="__main__":
    main()



