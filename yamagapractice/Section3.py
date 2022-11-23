
# coding:utf-8
#from curses.ascii import NUL
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
import SectionRun3
import SectionPrm3
#from yamagapractice import SectionRun2
#from Walker import Run
class Section3:
    #クラス変数
    NULL_PTR=0
    mSectionIdx=0
    sectionParam=SectionPrm3.SectionPrm3()
    UNDEFINED=0
    INIT=1
    RUN=2
    END=3
    mState=UNDEFINED
    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    section=[0,0]
    mlastIdx=0
    param=[None,None]
    mSection=SectionRun3.SectionRun3()
    msection=0
    Param=[None,None]
    runinstance_param=[None,None]
    judgeinstance_param=[None,None]
    count=[None]
    def __init__(self):
        #セクションパラメーターを初期化
        self.sectionParam.__init__()#Section
        pass

        #走法
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
            sys.exit()

    def execUndefined(self):
        self.mState=self.INIT#状態をINITにする
        

        pass

    def init(self):
        self.param[self.mSectionIdx]=self.get_param()#get_paramから値を取得
        flag=True

        while flag:

            self.addSection(self.param)#addセクションを回す
            
            self.mSectionIdx+=1
            
            if self.mSectionIdx==2:#もし引数が２だったらもう配列に入れれないためbreakする               print("NONE")
            #if self.param[self.mSectionIdx]==None:
                print("配列の限界")
                break
            else:
                pass

            self.param[self.mSectionIdx]=self.get_param()#値設定
            

        self.mState=self.RUN

    
        #セクション追加
    def addSection(self,param):
        #paramに値一つ
        self.setWalker(param)
        self.setjudge(param)
        
        
        self.section[self.mlastIdx]=None#sectionを埋める
        self.mlastIdx+=1 

        #return param[self.mlastIdx]
        
    
    def execRun(self):
        #print(self.mSection[self.mSectionIdx])
        print("exec",self.param)
        print("runinstance",self.runinstance_param)
        print("judeinstance",self.judgeinstance_param)
        print("count",self.count)
        self.mSection.run(self.judgeinstance_param,self.runinstance_param,self.count,self.param)
        self.mState=self.END



    def setWalker(self,param):
        #run=self.mSection.request_Walker(param[self.mSectionIdx])
        #self.instance_param[0]=self.mSection.request_Walker(param[self.mSectionIdx])

        if self.mSectionIdx==self.CURVE:
            self.runinstance_param[self.mSectionIdx]=self.mSection.request_Walker(self.mSectionIdx)
            #sectionRunでオブウジェクトが作れたらrun=にする。。と思う　以下も同じ
            param[self.mSectionIdx]=self.mSection.set_param(self.mSectionIdx)
            
        elif self.mSectionIdx==self.STRAIGHT:
            self.runinstance_param[self.mSectionIdx]=self.mSection.request_Walker(self.mSectionIdx)
            print("ooo",self.mSectionIdx)
            #self.mSection.request_Walker(param)
            self.count=self.mSection.count_set_param()
            param[self.mSectionIdx]=self.mSection.set_param(self.mSectionIdx)
        
        
        print("run",self.runinstance_param)
        print("cnt",self.count)#何秒走るか
    def setjudge(self,param):
        #run2=self.mSection.request_judge(param[self.mSectionIdx])
        
        if self.mSectionIdx==self.CURVE:

            self.judgeinstance_param[self.mSectionIdx]=self.mSection.request_judge(self.mSectionIdx)
            #run2.set_param(self.mSectionIdx)
        
        elif self.mSectionIdx==self.STRAIGHT:
            self.judgeinstance_param[self.mSectionIdx]=self.mSection.request_judge(self.mSectionIdx)
            print("ju",self.judgeinstance_param)
            #self.mSection.request_judge(param)
            #run2.set_param(self.mSectionIdx)
        #パラメータをSectionPrmからもらう
    def get_param(self):
        self.Param[self.mSectionIdx]=self.sectionParam.set_param(self.mSectionIdx)

        return self.Param[self.mSectionIdx]

def main():
    se=Section3()
    se.run()
    '''
    mSectionIdx=0
    se.get_param(mSectionIdx)
    mSectionIdx=1
    se.get_param(mSectionIdx)
    '''


if __name__=="__main__":
    main()



