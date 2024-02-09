
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
    section_set_Reiwa=[0,1,0,0,1,0]
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
        
        #print("走行のインスタンス",self.Walkerinstance)
        #print("判定のインスタンス",self.Judgeinstance)
        #print("positionMgmt",self.PositionMgmt)
        print("走行のパラメータ",self.WalkeParam)
        #print("座標",self.Pointer)
        
        
        print('state',self.WalkeParam[self.counter][4],'pointer',self.counter+1)
        
    def Run(self):
        
        
    
        if self.WalkeParam[self.counter][4]=='straight' or 'straight_right' or 'straight_left' :
        
            state=self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                                        self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt)
            #print("judge_time")
            if state==True: #goalしたかどうか
                self.Walkerinstance[self.STRAIGHT].init_state()
                print("Straight_OK!_Next_Section")
                
                
                if len(self.WalkeParam) != self.counter+1: #配列の長さを超えたか
                        
                    self.counter+=1
                    
                    print('state',self.WalkeParam[self.counter][4],'pointer',self.counter+1)
                    
                else:
                        if  self.number != 1 or 2 : #Circuit or etc
                            
                            self.end()
                                
                            return True
                            
                        else:
                            
                            self.counter=0
            else:
                
                #print("S_not_goal")
                
                pass
                
        else:
            
            state=self.sectionrun.run(self.Walkerinstance[self.CURVE],self.Judgeinstance[self.CURVE],
                                    self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt)
            
            if state==True:
                self.Walkerinstance[self.CURVE].init_state()
                print("Curve_OK!_Next_Section")
                
                
                if len(self.WalkeParam) != self.counter+1: #配列の要素があるか
                        
                    self.counter+=1
                    
                    print('state',self.WalkeParam[self.counter][4],'pointer',self.counter+1)
                    
                else:
                        if  self.number != 1 or 2 : #Circuit or etc
                            
                            self.end()
                                
                            return True
                            
                        else:
                            
                            self.counter=0
            else:
                
                #print("C_not_goal")
                
                pass

        

    def end(self):
        
        self.sectionrun.stop()
        
    

        
    def getWalker(self):
        
        
        self.Walkerinstance[self.STRAIGHT]=self.sectionrun.request_Walker(self.STRAIGHT)

        self.Walkerinstance[self.CURVE]=self.sectionrun.request_Walker(self.CURVE)



    def getJudge(self):
        
        self.Judgeinstance[self.STRAIGHT]=self.sectionrun.request_judge(self.STRAIGHT)
        
        self.Judgeinstance[self.CURVE]=self.sectionrun.request_judge(self.CURVE)


    def get_Param(self):
        
        
        self.WalkeParam=self.sectionparam.walkerset_param(self.number) #parameter,pointer,positionMgmt
        #print("param11111111111111111",self.WalkeParam)
        self.Pointer,self.PositionMgmt=self.sectionparam.pointer_param(self.number)
        
    
    def test(self):
        
        len=0
        if self.WalkeParam[self.counter][4]=='straight':
        
            state=self.sectionrun.run(self.Walkerinstance[self.STRAIGHT],self.Judgeinstance[self.STRAIGHT],
                                                            self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt)
                #print("judge_time")
            if state==True: #goalしたかどうか
                self.Walkerinstance[self.STRAIGHT].init_state()
                print("Straight_OK!_Next_Section")
                    
                    
                if len >= self.counter+1: #配列の長さを超えたか
                            
                    self.counter+=1
                        
                else:
                    
                    #self.sectionMgmt.end()
                        
                    return True
                            
            else:
                
                #print("S_not_goal")
                
                pass
                
        else:
            
            state=self.sectionrun.run(self.Walkerinstance[self.CURVE],self.Judgeinstance[self.CURVE],
                                    self.WalkeParam[self.counter],self.Pointer[self.counter],self.PositionMgmt)
            
            if state==True:
                self.Walkerinstance[self.CURVE].init_state()
                print("Curve_OK!_Next_Section")
                
                
                if len >= self.counter+1: #配列の要素があるか
                        
                    self.counter+=1
                    
                else:
                    self.sectionMgmt.end()
                            
                    return True
            else:
                
                #print("C_not_goal")
                
                pass
            
        

                
    def test2(self):
        
        while True:
        
            if self.WalkeParam[self.counter][4]=='straight':
            
                print(self.WalkeParam[self.counter],self.Pointer[self.counter])
                
                print("Straight_OK!_Next_Section")
                
                print(self.Pointer)
                    
                print("a",len(self.Pointer))    
                if len(self.Pointer) >= self.counter+1: #配列の長さを超えたか
                            
                        self.counter+=1
                        
                else:
                        if  self.number==3: #Circuit or etc
                                    
                            return True
                                
                        else:
                                
                            break
                
                    
                    #print("S_not_goal")
                    
                    
            else:
                
                print(self.WalkeParam[self.counter],self.Pointer[self.counter])
                
                    
                    
                if len(self.Pointer) >= self.counter+1: #配列の要素があるか
                            
                        self.counter+=1
                        
                else:
                            
                    if  self.number==3: #Circuit or etc
                                    
                        return True
                                
                    else:
                                
                        break


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
    sectionMgmt.preparation(1)
    #sectionMgmt.run()
    #sectionMgmt.execRun()
    #sectionMgmt.test1()
    #sectionMgmt.test2()
    

if __name__=="__main__":
    main()



