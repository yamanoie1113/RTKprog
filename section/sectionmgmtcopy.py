
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
    conter = 0
    sectionparam=SectionPrm.SectionPrm()
    sectionrun=SectionRun.SectionRun()
    STRAIGHT = 0
    CURVE = 1           #0は直線、1は曲線
    counter=0
    test0=None
    section_set=[0,1,0,0,1,0]    #0が直線　1が曲線
    section_set_Reiwa=[0,1,0,0,0,1,0,0,0]
    position=None
    PositionMgmt=None
    sectionpoint=0
    instancepoint=0
    Swalkerpointer=0 #6まで
    Cwalkerpointer=0 #2まで
    testsection=1
    
    def __init__(self):

        pass
    
    
    def run():
        
        #stateの切り替え
        '''
        #状態をINITにする
        #状態の分岐
        #状態がUNDEFINEDだったらexecUndefindを実行
        if self.mState == self.UNDEFINED:
            self.execUndefined()

        #状態がINITだったらinitを実行
        elif self.mState == self.INIT:
            self.init()

        #状態がRUNのだったらexecRunを実行
        elif self.mState == self.RUN:
            self.execRun()

        
        '''
        pass
        
        
    def addSection(self):
        self.get_Param()#座標、パラメータ
        self.setWalker()#instaance
        self.setJudge()#判定
        
        
        
    def addSection_R(self):
        
        self.get_Param_R()#座標、パラメータ
        self.setWalker()#instance
        self.setJudge()#判定
        
        
    def execRun(self):
        
        print("Walkerinstance:",self.Walkerinstance)
        print("judgeinstance",self.Judgeinstance)
        print("WalkerParam",self.WalkeParam)
        print("座標",self.Pointer)
        
        state=False
        
        if self.section_set[self.counter]==0:
        
            state=self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                                    self.WalkeParam[self.counter],self.Pointer[self.counter])
            
            if state==True:
                self.Walkerinstance[self.STRAIGHT].init_state()
                print("Straight_OK!_Next_Section")
                self.counter+=1
                
                if self.counter==6:
                    self.counter=0
                
        else:
            
            state=self.sectionrun.run(self.Walkerinstance[self.CURVE],self.Judgeinstance[self.CURVE],
                                                    self.WalkeParam[self.counter],self.Pointer[self.counter])
            
            if state==True:
                self.Walkerinstance[self.CURVE].init_state()
                print("Curve_OK!_Next_Section")
                self.counter+=1
                
                if self.counter==6:
                    self.counter=0
        
    def setWalker(self):
        
        
        self.Walkerinstance[self.STRAIGHT]=self.sectionrun.request_Walker(self.STRAIGHT)

        self.Walkerinstance[self.CURVE]=self.sectionrun.request_Walker(self.CURVE)



    def setJudge(self):
        
        self.Judgeinstance[self.STRAIGHT]=self.sectionrun.request_judge(self.STRAIGHT)
        
        self.Judgeinstance[self.CURVE]=self.sectionrun.request_judge(self.CURVE)

    def get_Param(self):
        
        self.WalkeParam=self.sectionparam()
        self.Pointer,self.PositionMgmt=self.sectionparam.pointer_param()
        
        
        
        
        
    def execRun_old(self):
        state=None
        #パラメータの配列を最初に戻すのを繰り返す
        
        if self.section_set[self.pointerset]==0: #直線の場合
            #print("straight:", self.pointerset)
            '''
            print("Walkerinstance:",self.Walkerinstance[self.STRAIGHT])
            print("judgeinstance",self.Judgeinstance[self.STRAIGHT])
            print("WalkerParam",self.WalkeParam[self.STRAIGHT][self.Swalkerpointer])
            print("座標",self.Pointer[self.pointerset])
            '''
            state=self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                    self.WalkeParam[self.STRAIGHT][self.Swalkerpointer],self.Pointer[self.pointerset],self.PositionMgmt) 
            if state==True:
                print("straight_OK")
                self.Walkerinstance[self.STRAIGHT].init_state()
                self.Swalkerpointer+=1
                if self.Swalkerpointer==4:
                    self.Swalkerpointer=0

                self.pointerset+=1
                    #print("pointer_count",self.pointerset)
                if self.pointerset==6:
                    self.pointerset=0
                

                
        else: #曲線
            #print("curve:", self.pointerset)
            '''
            print("Walkerinstance:",self.Walkerinstance[self.CURVE])
            print("judgeinstance",self.Judgeinstance[self.CURVE])
            print("WalkerParam",self.WalkeParam[self.CURVE][self.Cwalkerpointer])
            print("座標",self.Pointer[self.pointerset])
            '''
            #print("Curve_start")
            
            state=self.sectionrun.run(self.Walkerinstance[self.CURVE],self.Judgeinstance[self.CURVE],
                                    self.WalkeParam[self.CURVE][self.Cwalkerpointer],self.Pointer[self.pointerset],self.PositionMgmt)
            if state==True:
                print("Curve_OK")
                self.Walkerinstance[self.CURVE].init_state()
                self.Cwalkerpointer+=1
                if self.Cwalkerpointer==2:
                    self.Cwalkerpointer=0

                self.pointerset+=1
                if self.pointerset==6:
                    self.pointerset=0

        self.mState=self.END
        
    def excecRun_R(self):
        
        state_R=None
        
        if self.section_set_Reiwa[self.pointerset]==0: #直線の場合
            '''
            print("走行インスタンス",self.Walkerinstance[self.STRAIGHT])
            print("判定インスタンス",self.Judgeinstance[self.STRAIGHT])
            print("パラメータ",self.WalkeParam[self.STRAIGHT][self.Swalkerpointer])
            print("座標",self.Pointer[self.pointerset])
            '''
            state_R=self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                    self.WalkeParam[self.STRAIGHT][self.Swalkerpointer],self.Pointer[self.pointerset],self.PositionMgmt) 
            if state_R==True:
                print("Straight_OK")
                self.Walkerinstance[self.CURVE].init_state()
            
                self.Swalkerpointer+=1
                if self.Swalkerpointer==6:  
                    self.Swalkerpointer=0

                self.pointerset+=1
                if self.pointerset==8:
                    self.pointerset=0
                

                
        else: #曲線
            
            state_R=self.sectionrun.run(self.Walkerinstance[self.CURVE],self.Judgeinstance[self.CURVE],
                                    self.WalkeParam[self.CURVE][self.Cwalkerpointer],self.Pointer[self.pointerset],self.PositionMgmt)
            if state_R==True:
                print("Curve_OK")
                self.Walkerinstance[self.CURVE].init_state()
                
                self.Cwalkerpointer+=1
                if self.Cwalkerpointer==2:
                    self.Cwalkerpointer=0

                self.pointerset+=1
                if self.pointerset==8:
                    self.pointerset=0

        self.mState=self.END
        

    def end(self):
        
        self.sectionrun.stop()
        
        
        
        
    
    def end_REIWA(self):
        
        
        self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                    self.WalkeParam[self.STRAIGHT][self.Swalkerpointer],self.Pointer[self.pointerset],self.PositionMgmt) 
        self.sectionrun.stop()
        
        

    def setWalker(self):
        
        
        self.Walkerinstance[self.STRAIGHT]=self.sectionrun.request_Walker(self.STRAIGHT)

        self.Walkerinstance[self.CURVE]=self.sectionrun.request_Walker(self.CURVE)



    def setJudge(self):
        
        self.Judgeinstance[self.STRAIGHT]=self.sectionrun.request_judge(self.STRAIGHT)
        
        self.Judgeinstance[self.CURVE]=self.sectionrun.request_judge(self.CURVE)

    def get_Param(self):
        
        self.WalkeParam=self.sectionparam()
        self.Pointer,self.PositionMgmt=self.sectionparam.pointer_param()
        


    def get_Param_old(self):
        
        self.WalkeParam[self.STRAIGHT]=self.sectionparam.Walkerset_param(self.STRAIGHT)

        self.WalkeParam[self.CURVE]=self.sectionparam.Walkerset_param(self.CURVE)

        self.Pointer,self.PositionMgmt=self.sectionparam.pointer_param()
        
        
    def get_Param_R(self):
        
        self.WalkeParam[self.STRAIGHT]=self.sectionparam.walkerset_param_R(self.STRAIGHT)

        self.WalkeParam[self.CURVE]=self.sectionparam.walkerset_param_R(self.CURVE)

        self.Pointer,self.PositionMgmt=self.sectionparam.pointer_param_R()







def main():
    
    sectionMgmt=SectionMgmt()
    sectionMgmt.run()
    #sectionMgmt.execRun()
    #sectionMgmt.test1()
    #sectionMgmt.test2()
    

if __name__=="__main__":
    main()



