
from asyncio.windows_events import NULL
from curses.ascii import NUL
from section.SectionPrm import SectionPrm
from section.SectionRun import SectionRun
from Walker.Run import Run

class SectionMgmt:


    NULL_PTR=0
    mSectionIdx=0
    sectionParam=SectionPrm()
    UNDEFINED=0
    INIT=1
    RUN=2
    mState=UNDEFINED
    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    section=[]
    mlastIdx=0

    

    def __init__(self):
        self.sectionParam.init()

    def run(self):

       
        if self.mState == self.UNDEFINED:
            self.execUndefined()

        elif self.mState == self.INIT:
            self.init()

        elif self.mState == self.RUN:
            self.execRun()

    def execUndefined(self):
        
        self.mState=self.INIT

        pass

    def init(self):
        param=self.get_param()
        #addセクションを回す
        while(param[self.mSectionIdx]["flag"]):
            self.addSection(param[self.mSectionIdx][:])
            self.mSectionIdx+=1
            break
        self.mState=self.RUN
        pass

        #セクション追加
    def addSection(self,param):
        mSection=SectionRun()
        self.setWalker(mSection,param)
        self.setJudge(mSection,param)
        self.section[self.mlastIdx]=mSection
        self.mlastIdx+=1
        self.section[self.mlastIdx]=None
        

    def setWalker(self,mSection,param):
        
        run=mSection.request_Walker(param["walker"])
    
        if param["walker"]==self.CURVE:
            #パラメータ投げる
            print("a")
        elif param["walker"]==self.STRAIGHT:
            #パラメータ投げる
            print("b")

        pass

    def setJudge(self,mSection,param):

        judge=mSection.request_Judge(param["judge"])

        if param["judge"]==self.DISTANCE:
            judge.set_param(param["judgevalue"])
            
        elif param["judge"]==self.ANGLE: #複数ある可能性あり
            judge.set_param(param["judgevalue"])

        pass


    def execRun(self):

        if self.mSection[self.mSectionIdx] is None:
            return True

        if self.mSection[self.mSectionIdx].run():
            self.mSectionIdx+=1
            
        return False

    def get_param(self):
        param=self.sectionParam.get_param(self.mSectionIdx)
        return param

    def __del__(self):
        pass


