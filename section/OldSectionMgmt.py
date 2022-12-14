
# coding:utf-8
from asyncio.windows_events import NULL
#from curses.ascii import NUL
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import SectionPrm
from section import SectionRun
from Walker import Run
class SectionMgmt:
    #クラス変数
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
        #セクションパラメーターを初期化
        self.sectionParam.init()

    def run(self):

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

    def execUndefined(self):
        #状態をINITにする
        self.mState=self.INIT

        pass

    def init(self):
        #パラメータを設定する
        param=self.get_param()
        #addセクションを回す
        while(param[self.mSectionIdx]["flag"]):
            self.addSection(param[self.mSectionIdx][:])#addsection実行
            self.mSectionIdx+=1#プラスしていく
            break
        self.mState=self.RUN
        pass

        #セクション追加
    def addSection(self,param):
        mSection=SectionRun()#オブジェクト生成
        self.setWalker(mSection,param)#走法
        self.setJudge(mSection,param)#判定
        #msectionを入れる
        self.section[self.mlastIdx]=mSection
        self.mlastIdx+=1
        self.section[self.mlastIdx]=None
        
        

    def setWalker(self,mSection,param):
        

        run=mSection.request_Walker(param["walker"])
            #パラメータの判定
        if param["walker"]==self.CURVE:#0
            #曲線のパラメータ投げる
            run.set_param(param["walkervalue"])

        elif param["walker"]==self.STRAIGHT:#1
            #直線のパラメータ投げる

            run.set_param(param["walkervalue"])

        pass

    def setJudge(self,mSection,param):

        judge=mSection.request_Judge(param["judge"])

        if param["judge"]==self.DISTANCE:
            #パラメータ投げる
            judge.set_param(param["judgevalue"])

            #パラメータ投げる
        elif param["judge"]==self.ANGLE: #複数ある可能性あり
            judge.set_param(param["judgevalue"])

        pass

    def execRun(self):
        #msectionがNONEだったらTrueを返す
        if self.mSection[self.mSectionIdx] is None:
            return True

        if self.mSection[self.mSectionIdx].run():
            self.mSectionIdx+=1
            
        return False

        #パラメータをSectionPrmからもらう
    def get_param(self):
        param=self.sectionParam.set_param(self.mSectionIdx)
        return param

    def __del__(self):
        pass

def main():
    pass

if __name__=="__main__":
    main()




#init内でgetparam呼び出し
#getparamでパラメータ設定（paramに入る値は　　　　)
#addsectionに移る
#SectionRunオブジェクト生成

