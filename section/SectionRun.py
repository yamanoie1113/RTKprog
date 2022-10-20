# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#from Sensors import MotorMgmt
#from Walker import Run
from Walker import VirtualLineTrace
from Walker import VirtualLineTrace2
from Judgement import DistanceJudge
from Judgement import TurnAngleJudge



class SectionRun:

    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    judgefirst=True
    walkerfirst=True
    mWalker=0
    mjudge=0
    #mMotorMgmt=MotorMgmt()
    def run(self):
        
        #if self.judgefast:

        pass

    def request_Walker(self,walker):

    #走法の生成依頼

        if walker==self.CURVE:
            self.mWalker=VirtualLineTrace()
            #self.mWalker=Run(self.mMotorMgmt)
        elif walker==self.STRAIGHT:
            self.mWalker=VirtualLineTrace2()
        
        return self.mWalker

    def request_judge(self,judge):

        #判定の生成依頼

        if judge==self.DISTANCE:
            self.mJudge=DistanceJudge()
        elif judge==self.ANGLE:
            self.mJudge=TurnAngleJudge()

        return self.mJudge

def main():
    
    pass

if __name__=="__main__":
    main()