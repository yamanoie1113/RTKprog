
# coding:utf-8
#from curses.ascii import NUL
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import SectionRunTest
from section import SectionPrm2
#import SectionPrm2
#from yamagapractice import SectionRun2
#from Walker import Run
class SectionMgmtTest:
    #クラス変数
    UNDEFINED=0
    INIT=1
    RUN=2
    END=3
    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    tttt=0
    mcounter=0
    #mSection=SectionRun2.SectionRun2()
    def __init__(self):
        self.NULL_PTR=0
        self.mSectionIdx=0
        self.sectionParam=SectionPrm2.SectionPrm2()
        self.mSection=SectionRunTest.SectionRunTest()
        self.mState=self.UNDEFINED
        self.section=[0,0]
        print("haaaaaaaaaaaaaaaaaaaa",self.mcounter)
        #self.mcounter=+1
        self.mlastIdx=0
        self.param=[None,None]
        self.tttt+=1
        print("mcountttttttttttt",self.mcounter)

        self.msection=0
        self.Param=[None,None]
        self.runinstance_param=[None,None]
        self.judgeinstance_param=[None,None]
        self.count=[None,None]

        
    #def __init__(self):
        #セクションパラメーターを初期化
        #self.sectionParam.__init__()#Section
        #self.mSection.__init__()

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
            print("どうだaaaaaaaaaaaaaaaaaaaaaaaaaa",self.mcounter)
            self.ini()

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

    def ini(self):
        self.param[self.mSectionIdx]=self.get_param()#get_paramから値を取得
        flag=True
        self.mcounter-=1

        while flag:

            self.addSection(self.param)#addセクションを回す
            
            self.mSectionIdx+=1
            print("kokokokokoko",self.mSectionIdx)
            if self.mSectionIdx==2:#もし引数が２だったらもう配列に入れれないためbreakする               print("NONE")
            #if self.param[self.mSectionIdx]==None:
                print("配列の限界")
                flag=False
                if flag==False:
                    break
                else:
                    pass
                
            else:
                pass

            #self.param[self.mSectionIdx]=self.get_param()#値設定
        
        #self.mcount=self.upgrade_mcount()
        print("mcountだよ",self.mcounter)#mcountは走法、判定、カウントのパラメータの配列を順番に取り出すやつ
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
        print("count",self.count[0])
        print("count",self.count[1])
        print("countall",self.count)
        print("cnt",self.mcounter)
        #デバッグ
        if (self.param[0]==None) or (self.param[1]==None) :
            print("None")
            self.mcounter-=1
        elif (self.count[0]==None) or (self.count[1]==None):
            self.mcounter-=1
            print("None")
        print("こらああああああああああああああああ",self.mcounter)   
        self.mSection.run(self.judgeinstance_param,self.runinstance_param,self.count,self.param)#えらーになったらself.runinstance_paramを一回外してください
        self.mcounter+=1
        self.mState=self.END



    def setWalker(self,param):
        #run=self.mSection.request_Walker(param[self.mSectionIdx])
        #self.instance_param[0]=self.mSection.request_Walker(param[self.mSectionIdx])
            print("aaaaaaaaaaaaaaaa",self.mcounter)
            if self.mSectionIdx==self.CURVE:
                self.runinstance_param[self.mSectionIdx]=self.mSection.request_Walker(self.mSectionIdx)
                #sectionRunでオブウジェクトが作れたらrun=にする。。と思う　以下も同じ
                param[self.mSectionIdx]=self.mSection.set_param(self.mSectionIdx,self.mcounter)
                self.count[self.mSectionIdx]=self.mSection.count_set_param1(self.mcounter)
                print("konoyaroumeee",self.count)
            elif self.mSectionIdx==self.STRAIGHT:
                self.runinstance_param[self.mSectionIdx]=self.mSection.request_Walker(self.mSectionIdx)
                print("ooo",self.mSectionIdx)
                print("self.mcountdaaaaaaa",self.mcounter)
                param[self.mSectionIdx]=self.mSection.set_param(self.mSectionIdx,self.mcounter)
                self.count[self.mSectionIdx]=self.mSection.count_set_param2(self.mcounter)
                print("カウントだい",self.count)
                #self.mSection.request_Walker(param)
            
    
            print("run",self.runinstance_param)
            print("self.mcountだいいい",self.mcounter)
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
    se=SectionMgmtTest()
    se.run()
    '''
    mSectionIdx=0
    se.get_param(mSectionIdx)
    mSectionIdx=1
    se.get_param(mSectionIdx)
    '''


if __name__=="__main__":
    main()



