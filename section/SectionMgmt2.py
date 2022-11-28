
# coding:utf-8
#from curses.ascii import NUL
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import SectionRun2
from section import SectionPrm2
#import SectionPrm2
#from yamagapractice import SectionRun2
#from Walker import Run
class SectionMgmt2:
    #クラス変数
    UNDEFINED=0
    INIT=1
    RUN=2
    END=3
    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    mcount=0
    
    #mSection=SectionRun2.SectionRun2()
    def __init__(self):
        self.NULL_PTR=0
        self.mSectionIdx=0
        self.sectionParam=SectionPrm2.SectionPrm2()
        self.mSection=SectionRun2.SectionRun2()
        self.mState=self.UNDEFINED
        self.section=[0,0]
        self.mlastIdx=0
        self.param=[None,None]
        
        self.msection=0
        self.Param=[None,None]
        self.runinstance_param=[None,None]
        self.judgeinstance_param=[None,None]
        self.count=[None,None]
    #def __init__(self):
        #セクションパラメーターを初期化
        self.sectionParam.__init__()#Sectionparam2
        self.mSection.__init__()#SectionRun2

        print("プリント")
        self.mState=self.UNDEFINED
        self.run()
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
            print("おわり")
            self.end()
            #sys.exit()
        else:
            pass

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

            #self.param[self.mSectionIdx]=self.get_param()#値設定
            
        self.mcount+=1
        print("mcountだよ",self.mcount)#mcountは走法、判定、カウントのパラメータの配列を順番に取り出すやつ
        self.mState=self.RUN

    
        #セクション追加
    def addSection(self,param):
        #paramに値一つ
        self.setWalker(param)
        self.setjudge()
        
        #self.count=self.mSection.count_set_param(self.mcount)
        
        self.section[self.mlastIdx]=None#sectionを埋める
        self.mlastIdx+=1 
        
        #return param[self.mlastIdx]
        
    
    def execRun(self):
        #print(self.mSection[self.mSectionIdx])
        print("exec",self.param)
        print("runinstance",self.runinstance_param)
        print("judeinstance",self.judgeinstance_param)
        print("count",self.count)
        print("cnt",self.mcount)
        #デバッグ
        if self.param[0]==None or self.param[1]==None:
            self.mcount=0
        elif self.count[0]==None or self.count[1]==None:
            self.mcount=0
            
        else:
            self.mSection.run(self.judgeinstance_param,self.runinstance_param,self.count,self.param)#えらーになったらself.runinstance_paramを一回外してください
        
        self.mState=self.END



    def setWalker(self,param):
        #run=self.mSection.request_Walker(param[self.mSectionIdx])
        #self.instance_param[0]=self.mSection.request_Walker(param[self.mSectionIdx])

        if self.mSectionIdx==self.CURVE:
            self.runinstance_param[self.mSectionIdx]=self.mSection.request_Walker(self.mSectionIdx)
            #sectionRunでオブウジェクトが作れたらrun=にする。。と思う　以下も同じ
            param[self.mSectionIdx]=self.mSection.set_param(self.mSectionIdx,self.mcount)
            self.count[self.mSectionIdx]=self.mSection.count_set_param1(self.mcount)
            
        elif self.mSectionIdx==self.STRAIGHT:
            self.runinstance_param[self.mSectionIdx]=self.mSection.request_Walker(self.mSectionIdx)
            print("ooo",self.mSectionIdx)
            print("self.mcountdaaaaaaaaaaaaaaaaaaaaa",self.mcount)
            param[self.mSectionIdx]=self.mSection.set_param(self.mSectionIdx,self.mcount)
            self.count[self.mSectionIdx]=self.mSection.count_set_param2(self.mcount)
            
            #self.mSection.request_Walker(param)
            
        
        print("run",self.runinstance_param)
        print("count",self.count)#何秒走るか
    def setjudge(self):
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

    def end(self):
        print("エンド")
        pass

def main():
    se=SectionMgmt2()
    se.run()
    '''
    mSectionIdx=0
    se.get_param(mSectionIdx)
    mSectionIdx=1
    se.get_param(mSectionIdx)
    '''


if __name__=="__main__":
    main()



