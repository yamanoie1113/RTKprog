# coding:utf-8
from asyncio.windows_events import NULL
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#from Sensors import MotorMgmt
#from Walker import Run
#from Walker import VirtualLineTrace
#from Walker import curveLineTrace
#from Judgement import DistanceJudge
#from Judgement import TurnAngleJudge



class SectionRun2:

    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    judgefirst=True
    walkerfirst=True
    mWalker=0
    mjudge=0
    #mMotorMgmt=MotorMgmt()
    def run(self):#作成中
        
        #判定
        if self.judgefirst:#truekafalseか
            self.mjudge.init()
            #if self.ajudge !=None: #ajudgeはどうすれば？
                #self.aJudge.init()
            #self.judgefirst= False
        if self.mjudge.run():
            
            return  True
        #走法
        if self.walkerfirst:
            self.mWalker.init()
            self.walkerfirst=False

        self.mWalker.run()
            
    def request_Walker(self,walker):

    #走法の生成依頼

        if walker==self.CURVE:
            #self.mWalker=VirtualLineTrace()
            print("curve")
            #self.mWalker=Run(self.mMotorMgmt)
            #self.run()
        elif walker==self.STRAIGHT:
            #self.mWalker=curveLineTrace()
            print("straight")
        
        return self.mWalker

    def request_judge(self,judge):

        #判定の生成依頼

        if judge==self.DISTANCE:
            #self.mJudge=DistanceJudge()
            print("judge")
        elif judge==self.ANGLE:
            #self.mJudge=TurnAngleJudge()
            print("mjudghe")

        return self.mJudge

    #def set_param(self,param):
        #if param==0:
            #print(4)
            #self.run(param)
        #else:
        #print(2)
        # self.run(param)
        
    def i(self,p):
        print("i=",p)



def main():
    
    pass

if __name__=="__main__":
    main()