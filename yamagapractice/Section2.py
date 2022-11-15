
# coding:utf-8
#from curses.ascii import NUL
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
import SectionRun2
import SectionPrm2
#from yamagapractice import SectionRun2
#from Walker import Run
class Section2:
    #クラス変数
    NULL_PTR=0
    mSectionIdx=0
    sectionParam=SectionPrm2.SectionPrm2()
    UNDEFINED=0
    INIT=1
    RUN=2
    END=3
    mState=UNDEFINED
    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    section=[0,1]
    mlastIdx=-1
    param=[0,0]
    mSection=SectionRun2.SectionRun2()
    msection=0

    def __init__(self):
        #セクションパラメーターを初期化
        self.sectionParam.__init__()
        pass

        #走法
    def run(self):
        if self.mState == self.UNDEFINED:
            print(self.mState)
            self.execUndefined()
        else:
            pass

        if self.mState == self.INIT:
            print("initだよ")
            self.init()

        else:
            pass
        
        if self.mState == self.RUN:
            self.execRun()
        
        else:
            pass

        if self.mState==self.END:
            sys.exit()

    def execUndefined(self):
        self.mState=self.INIT#状態をINITにする
        print("ex",self.mState)

        pass

    def init(self):
        self.param[self.mSectionIdx]=self.get_param()#get_paramから値を取得
        flag=True
        while flag:
            self.addSection(self.param[self.mSectionIdx])#addセクションを回す
            self.mSectionIdx+=1

            if self.mSectionIdx==2:#もし引数が２だったらもう配列に入れれないためbreakする               print("NONE")
            #if self.param[self.mSectionIdx]==None:
                break
            else:
                self.param[self.mSectionIdx]=self.get_param()#値設定
                pass

        #self.mState=self.RUN
        pass

        #self.mState=self.RUN
    
        pass


        

    
        #セクション追加
    def addSection(self,param):
        #paramに値一つ
        self.setWalker(param)
        self.setjudge(param)
        #self.execRun()
        self.section[self.mlastIdx]=None#sectionを埋める

        return param
        
    
    def execRun(self):
        #print(self.mSection[self.mSectionIdx])
        print("exec")
        #runメソッド呼ぶ
        #ここで走るんじゃなかろうか
        #
        
        pass

        

        

        self.mState=self.END

        pass


    def setWalker(self,param):
        #run=self.mSection.request_Walker(param[self.mSectionIdx])
        if param==self.CURVE:
            print("allgrenn")
            self.mSection.request_Walker(param)
            pass
        
        elif param==self.STRAIGHT:
            print("allgreen2")
            self.mSection.request_Walker(param)

            pass
            

    def setjudge(self,param):

        if param==self.CURVE:
            print("judgeallgrenn")
            self.mSection.request_judge(param)
            pass
        
        elif param==self.STRAIGHT:
            print("judgeallgreen2")
            self.mSection.request_judge(param)

            pass

        #パラメータをSectionPrmからもらう
    def get_param(self):
        
        self.Param=self.sectionParam.set_param(self.mSectionIdx)
        print("naice",self.Param)

        return self.Param

def main():
    se=Section2()
    se.run()
    pass


if __name__=="__main__":
    main()



