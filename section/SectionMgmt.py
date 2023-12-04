
# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import SectionRun
from section import SectionPrm
#from Walker import Run

class SectionMgmt:

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
    param = []
    
    def __init__(self):

        pass
        
        
    def preparation(self,course_select): #走行準備
        
        self.number=course_select
        self.get_Param()#パラメータ、座標
        self.getWalker()#instaance
        self.getJudge()#判定
        
        
        
    def Run(self):
        
        print("走行のインスタンス",self.Walkerinstance)
        print("判定のインスタンス",self.Judgeinstance)
        print("走行のパラメータ",self.WalkeParam)
        print("座標",self.Pointer)
        #self.PositionMgmt=インスタンス
        
        #if self.number != 3:
            
        if self.WalkeParam[self.Pointer][4]=='straight':
        
            state=self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                                        self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt)
                
            if state==True: #goalしたかどうか
                self.Walkerinstance[self.STRAIGHT].init_state()
                print("Straight_OK!_Next_Section")
                
                    
                if len(self.Pointer) >= self.counter+1: #配列の長さを超えたか
                        
                    self.counter+=1
                    
                else:
                        if  self.number==3: #Circuit or etc
                                
                            return True
                            
                        else:
                            
                            self.counter=0
                
        else:
            
            state=self.sectionrun.run(self.Walkerinstance[self.CURVE],self.Judgeinstance[self.CURVE],
                                                    self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt)
            
            if state==True:
                self.Walkerinstance[self.CURVE].init_state()
                print("Curve_OK!_Next_Section")
                
                
                if len(self.Pointer) >= self.counter+1: #配列の要素があるか
                        
                    self.counter+=1
                    
                else:
                        if  self.number==3: #Circuit or etc
                                
                            return True
                            
                        else:
                            
                            self.counter=0
    '''
    def circuit_run(self):
        
            state=self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                                    self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt)
            
            if state==True:
                self.Walkerinstance[self.CURVE].init_state()
                print("Curve_OK!_Next_Section")
                self.counter+=1
                    
                if len(self.Pointer) >= self.counter+1:
                    
                    break
            
            return True
    '''
        
    def getWalker(self):
        
        
        self.Walkerinstance[self.STRAIGHT]=self.sectionrun.request_Walker(self.STRAIGHT)

        self.Walkerinstance[self.CURVE]=self.sectionrun.request_Walker(self.CURVE)



    def getJudge(self):
        
        self.Judgeinstance[self.STRAIGHT]=self.sectionrun.request_judge(self.STRAIGHT)
        
        self.Judgeinstance[self.CURVE]=self.sectionrun.request_judge(self.CURVE)


    def get_Param(self):
        
        
        self.WalkeParam=self.sectionparam(self.number) #parameter,pointer,positionMgmt
        self.Pointer,self.PositionMgmt=self.sectionparam.pointer_param()
        
        
        
    def excecRun_R(self):
        
        print("Walkerinstance:",self.Walkerinstance)
        print("judgeinstance",self.Judgeinstance)
        print("WalkerParam",self.WalkeParam)
        print("座標",self.Pointer)
        
        state=False
        
        if self.section_set[self.counter]==0:
        
            state=self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                                    self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt)
            
            if state==True:
                self.Walkerinstance[self.STRAIGHT].init_state()
                print("Straight_OK!_Next_Section")
                self.counter+=1
                
                if self.counter==8:
                    self.counter=0
                
        else:
            
            state=self.sectionrun.run(self.Walkerinstance[self.CURVE],self.Judgeinstance[self.CURVE],
                                                    self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt)
            
            if state==True:
                self.Walkerinstance[self.CURVE].init_state()
                print("Curve_OK!_Next_Section")
                self.counter+=1
                
                if self.counter==8:
                    self.counter=0
        
        
        

    
        
        

    def end(self):
        
        self.sectionrun.stop()
        
        '''
        終了時の中心点停止処理
        self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                    self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt) 
        '''
        
        
    def end_REIWA(self):
        
        '''
        終了時の中心点停止処理
        self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                    self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt) 
        '''
        self.sectionrun.stop()






def main():
    
    sectionMgmt=SectionMgmt()
    sectionMgmt.run()
    #sectionMgmt.execRun()
    #sectionMgmt.test1()
    #sectionMgmt.test2()
    

if __name__=="__main__":
    main()



