
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
    mState=UNDEFINED
    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    section=[]
    mlastIdx=0
    param=[]
    mSection=SectionRun2.SectionRun2()
    def __init__(self):
        #セクションパラメーターを初期化
        self.sectionParam.__init__()
        pass

    def run(self):

        pass

    def execUndefined(self):
        

        pass

    def init(self):
        pass

        #セクション追加
    def addSection(self,param):
    
        pass
        


    def execRun(self):
        pass

    def setWalker(self,param):

        run=self.mSection.request_Walker(param)
        print(run)
            #パラメータの判定
        #if param[]==self.CURVE:#0
            #曲線のパラメータ投げる
            #run.set_param(param["walkervalue"])
        print("setwalker",param)
        #else:
            #pass
        #elif param["walker"]==self.STRAIGHT:#1
            #直線のパラメータ投げる
            #print("setwalker2",param)
            #run.set_param(param["walkervalue"])
        
        self.i=4
        self.mSection.i(self.i)
        
        pass

        #パラメータをSectionPrmからもらう
    def get_param(self):
        self.param=self.sectionParam.set_param(self.mSectionIdx)
        print("a",self.param)
        #self.setWalker(self.param)
        #return param

    def __del__(self):
        pass

def main():
    
    se=Section2()
    se.get_param()
    
    

if __name__=="__main__":
    main()



